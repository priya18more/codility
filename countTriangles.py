A = [10,2,5,1,8,12]


def countTriangles(A):
    A = sorted(A)
    triangles = 0

    for catBack in range(len(A)-2):
        catFront = catBack + 2
        for m in range(catBack + 1, len(A) - 1):
            while(catFront < len(A) and A[catBack] + A[m] > A[catFront]):
                catFront += 1
            triangles += catFront - m - 1
    return triangles



print(countTriangles(A))