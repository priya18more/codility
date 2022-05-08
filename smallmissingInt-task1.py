'''
array of an integer returns smallest (>0) positive integer that doesn't occur in A
'''
A = [-3,6,4,5,2,3]

def smallIntMissing(A):
    A = set(A)
    A = sorted(A)
    print(A)
    # array contains all negative values
    if max(A) <= 0:
        return 1
    sInt = False
    for i in range(len(A)):
        if A[i] == 1:
            sInt = True
    if sInt == False:
        return 1
    for i in range(len(A) -1):
        if A[i] > 0 and A[i + 1] - A[i] > 1:
            return A[i] + 1
    return A[len(A) - 1] + 1


print(smallIntMissing(A))