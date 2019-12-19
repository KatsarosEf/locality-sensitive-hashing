import numpy as np
from minhash import minHashing
from lsh import LSH
import argparse


def run(dataPath):
    nrofBands = 25
    nrOfPerms = 132
    nrOfRows = int(nrOfPerms/nrofBands)

    # Load data
    data = np.load(dataPath)
    print("Data is loaded")

    # Create an empty file to add results
    with open('results.txt', 'w') as file:
        file.write("")
        file.close()

    # Create Signature Matrix
    signatureMatrix = minHashing(data, nrOfPerms)
    pairsFound = LSH(data, signatureMatrix, nrOfRows, nrofBands)
    print(" Number of similar pairs found is : ", len(pairsFound))
    return(pairsFound)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Locality Sensitive Hashing')
    parser.add_argument('--file', type=str, help='data path')

    args = parser.parse_args()
    run(args.file)
