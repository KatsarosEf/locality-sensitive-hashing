# locality-sensitive-hashing

This is a python implementation of the Locality Sensitive Hashing algorithm to efficiently detect pais of similar users based on the Jaccard similarity. Initially implemented for the Netflix Prize dataset that is no longer available. Applicable on whichever boolean matrix (n, p). This implementation makes use of the efficient numpy library. We use np.bincount() and np.cumsum() to efficiently index and iterate.
