
A = [10,1,5,1,8,20]

def triangle(A):
    A = sorted(A)
    if len(A) < 3:
        return 0
    for i in range(len(A) - 2):
        if (A[i] + A[i + 1] > A[i + 2]):
            return 1
    return 0

print(triangle(A))