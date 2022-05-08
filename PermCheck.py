
A = [4,1,2,1]

def permCheck(A):
    if A:
        n = len(A)
        sumN = (n*(n+1))/2
        uniqA = set(A)
        if sumN == sum(A) and n == len(uniqA):
            return 1
        else:
            return 0
    else:
        return 0

print(permCheck(A))