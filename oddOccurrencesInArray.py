A = [9,3,9,3,9,7,9,7,4]

def oddOccurrence(A):
    '''
    if A:
        dict1 = {}
        for i in A:
            if i in dict1:
                dict1[i] = dict1.get(i,0) + 1
            else:
                dict1[i] = 1
        print(dict1)
        for key in dict1.keys() :
            if (dict1[key] % 2) != 0:
                print(key)
    '''
    if A:
        if len(A) == 1:
            print(A[0])
        else:
            A.sort()
            print(A)
            for i in range(0, len(A)-1, 2):
                if (A[i] != A[i+1]):
                    return A[i]
            return A[-1]



print(oddOccurrence(A))