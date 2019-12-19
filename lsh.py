import numpy as np
import time
from utils import writePair, jaccardIndex, combs



def LSH(data, signatureMatrix, nrOfRows, nrofBands):
    'Perform LSH on the given dataset'

    # Initializations

    nrofUsers = len(np.unique(data[:,0]))
    cumSums = np.cumsum(np.bincount(data[:,0]))
    indices = np.hstack((np.zeros(1), cumSums)).astype(int)
    row = 0
    pairsList = {}


    beginLSH = time.time()
    for band in range(nrofBands):

        # Make two dictionaries. 'Buckets' is the full dictionary, whereas
        # 'nonEmptyBuckets' is a subset containing only the keys that have more
        # than one values. We are looping on the latter for efficiency.

        buckets = {}
        nonEmptyBuckets = {}

        print(" Exploring Band : ", band, "...")
        for user in range(nrofUsers):
            bucketIds = tuple(signatureMatrix[row:row+nrOfRows, user])
            if bucketIds in buckets:
                buckets[bucketIds].append(user)
                nonEmptyBuckets[bucketIds] = 1
            else:
                buckets[bucketIds] = []
                buckets[bucketIds].append(user)
        row += nrOfRows

        # Loop on the small dictionary. Make a temp matrix to store the
        # users columns of the pairs in each bucket and map the new indices.
        #  Again, this avoids looping on the whole Signatures matrix.

        for bucket in nonEmptyBuckets.keys():
            tempMat = signatureMatrix[:,buckets[bucket]]
            tempInd = range(len(buckets[bucket]))
            pairs = combs(tempInd)

            for pair in pairs:

                # Check whether 'pair' is not found already. If found before
                # skip it, else procceed to estimate Jaccard Similarity
                # according to the Theorem.
                try:
                    test = pairsList[(buckets[bucket][pair[0]], buckets[bucket][pair[1]])]
                except KeyError:
                    (i, j) = pair

                    # Use the subMatrix of the signature matrix defined above.
                    # Note that we set the threshold to 0.45 so as to get more
                    # pairs, given that time allows for that.

                    if (np.mean(tempMat[:,i]==tempMat[:,j])) >= 0.45:

                        # Get back the initial indices for which we compute
                        # the actual Jaccard similarity.

                        (user1, user2) = (buckets[bucket][i], buckets[bucket][j])
                        jaccSim = jaccardIndex(data, indices, user1, user2)

                        if jaccSim >= 0.5:
                            # Write the pair if similarity is above the required threshold.
                            pairsList.update({(user1, user2):""})
                            writePair(user1, user2)

    totalTimee = np.round((time.time() - beginLSH)/60, 2)
    print(totalTimee, " Minutes elapsed for LSH in total : ")
    return(pairsList.keys())

