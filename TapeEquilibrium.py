A = [3,1,2,4,3]

def tapeEqui(A):
    '''
    brute solution

    absDiff = []
    for P in range(1,len(A)):
        print(A[:P])
        print(A[P:])
        print(sum(A))
        Diff = abs(sum(A[:P]) - sum(A[P:]))
        print(Diff)
        absDiff.append(Diff)
    print(absDiff)
    return min(absDiff)
    '''
    '''
    efficient algo
    '''
    minDiff = 20000
    s = sum(A)
    SL = 0
    for P in range(0,len(A)-1):
        SL+=A[P]
        Diff = abs(2*SL-s)
        minDiff = min(minDiff, Diff)
    return minDiff

print(tapeEqui(A))