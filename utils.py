import numpy as np
from itertools import combinations

def writePair(user1, user2):

    'Write Pair of users seperated by comma and close the file'

    f = open("results.txt", "a")
    f.write(str(user1) + "," + str(user2) + "\n")
    f.close()

def jaccardIndex(data, indices, user1, user2):

    'Compute Jaccard Similarities of users given their cumulative summations'

    moviesW1 = data[indices[user1]:indices[user1 + 1], 1]
    moviesW2 = data[indices[user2]:indices[user2 + 1], 1]
    
    return(len(np.intersect1d(moviesW1, moviesW2)) / len(np.union1d(moviesW1, moviesW2)) )

def combs(bucketValues):

    'Takes lists or 1-d arrays and outputs all possible pairwise combinations'

    return(list(combinations((bucketValues), 2)))
