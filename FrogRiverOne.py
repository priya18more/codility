'''
A[time] = position
A = [1,1,2,5,3,4,3]

B [position] = time
B = [0,2,4,5,3]
'''

A = [1,3,1,4,2,3,5,4]
X = 5

def riverCross(X, A):
    '''
    solution 1
    '''
    B = [0]*X
    s = 0
    for i in range(0,len(A)):
        if (B[A[i]-1] == 0 and A[i]<=X):
            s+=1
            B[A[i]-1] = 1
            print(B)
        if(s==X):
            return i
    return -1

def riverCross1(X,A):
    '''
    solution 2
    '''
    B=[-1]*X
    maxP = 0

    for i in range(len(A)):
        if (A[i]<=X and B[A[i]-1] == -1):
            B[A[i]-1]=i
    print(B)
    for i in range(len(B)):
        if B[i] == -1:
            return -1
        maxP = max(maxP,B[i])
    return maxP

def riverCross2(X,A):
    '''
    Solution 3
    '''
    position = ['f'] * (X+1)
    for time in range(len(A)):
        if position[A[time]] == 'f':
            position[A[time]] = 't'
            X -= 1

        if X == 0:
            return time
    return -1
print(riverCross(X,A))
print(riverCross1(X,A))
print(riverCross2(X,A))