
A = [3,2,-6,4,0]

def maxSliceSum(A):
    maxValue = A[0]
    sum = A[0]

    for i in range(1,len(A)):
        maxValue = max(A[i], maxValue + A[i])
        sum = max(sum, maxValue)
    return sum

print(maxSliceSum(A))