import numpy as np

def minHashing(data, nrofPerms):

    'Computes matrice of Signatures according to which we can estimate Jaccard similarities'

    # Initializations

    rowsToPerm = np.unique(data[:,1])
    nrofUsers = len(np.unique(data[:,0]))

    # Cumsum to avoid looping and Sparse matrices. We only use the initial dataset
    # and do not store the elements in matrix-form. Even with a sparse matrix
    # we would need to sparse.find(matrix) which gives tuple of indices and
    # respective values (0 or 1 here) and occupy the same amount of memory
    # with our implementation.

    cumSums = np.cumsum(np.bincount(data[:,0]))
    indices = np.hstack((np.zeros(1), cumSums)).astype(int)

    # Permutations defined. Note that we are making a signature matrix of size
    # nxPermutations and not its transposed, as operations are cheaper row-wisely.

    permuT = np.zeros((len(rowsToPerm), nrofPerms)).astype(int)
    for i in range(nrofPerms):
        permuT[:,i] = np.random.permutation(rowsToPerm)

    # Make the Signature matrix

    signMat = np.full((nrofPerms, nrofUsers), np.inf)
    for index in range(len(indices[:-1])):

        # Having the indices already, we can slice the matrix efficiently
        # and extract all the movies for a specific user without actually looping.
        # Then we apply the permutations and take the minimum position per User.

        moviesW = data[indices[index]:indices[index + 1]][:,1]
        colMins = np.min(permuT[moviesW,:], axis = 0)
        signMat[:,index] = colMins

    print(" Signature Matrix is created")
    return(signMat)
