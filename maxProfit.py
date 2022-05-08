
A = [23171,21011,21123,21366,21013,21367]

def maxProfit(A):
    maxP = 0
    maxSlice = 0
    N = len(A)
    if N == 0:
        return 0

    for i in range(1,N):
        d = A[i] - A[i -1]
        maxP = max(d, maxP + d)
        maxSlice = max(maxSlice, maxP)
    return maxSlice


print(maxProfit(A))