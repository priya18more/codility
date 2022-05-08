
A = [3,2,6,-1,4,5,-1,2]

def maxDoubleSliceSum(A):
    maxStartingHere = [0] * len(A)
    maxEndingHere = [0] * len(A)
    maxSum = 0
    len1 = len(A)

    for i in range(len1-2,1,-1):
        maxSum = max(0,A[i] + maxSum)
        maxStartingHere[i] = maxSum
    print(maxStartingHere)

    maxSum = 0

    for i in range(1,len1-1):
        maxSum = max(0,A[i] + maxSum)
        maxEndingHere[i] = maxSum
    print(maxEndingHere)
    maxDoubleSlice = 0

    for i in range(len1-2):
        maxDoubleSlice = max(maxDoubleSlice, maxStartingHere[i+2] + maxEndingHere[i])

    return maxDoubleSlice


print(maxDoubleSliceSum(A))