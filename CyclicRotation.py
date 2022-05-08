
A = [3, 8, 9, 7, 6]
K = 3
A1 = []
def CyclicRotation(A,K):
    if A :
        for i in range(K):
            A.insert(0, A.pop())
        return A
    else:
        return A



CyclicRotation(A1,K)