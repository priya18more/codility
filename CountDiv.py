
A = 6
B = 11
K = 2

def countDiv(A,B,K):
    '''
    brute solution
    '''
    count = 0
    for i in range(A,B):
        if (i % K) == 0:
            count += 1
    return count

def countDiv1(A,B,K):
    '''
    optimize solution
    '''
    count = int((B/K)) - int((A/K))
    if (A%K) == 0:
        count += 1
    return count

print(countDiv(A,B,K))
print(countDiv1(A,B,K))