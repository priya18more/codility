
A = [-3,1,2,-2,5,6]

def maxProduct(A):
    A = sorted(A)
    N = len(A)
    P1 = A[0] * A[1] * A[N-1]
    P2 = A[N-3] * A[N-2] * A[N-1]
    return max(P1,P2)

print(maxProduct(A))