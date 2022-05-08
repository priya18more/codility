
A = [-1,6,3,4,7,4]

def ArrayInversionCount(A):
    '''
    brute solution
    '''
    mapArray = []
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                mapArray.append((i, j))
    print(mapArray)
    '''
    optimise method : merge sort, AVL, Binary Index Tree
    '''




ArrayInversionCount(A)