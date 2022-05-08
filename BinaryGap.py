import math
import re
N = 1043


def BinaryGap(N):
    if N > 0:
        BinN = bin(N)[2:]
        print(BinN)
        bCount = 0
        maxB = 0
        for i in BinN:
            print(i)
            if i == '0':
                bCount += 1
                print(bCount)
            elif i == '1':
                maxB = max(bCount, maxB)
                bCount = 0
                print(maxB)
            else:
                return 0
        return maxB

print(BinaryGap(N))