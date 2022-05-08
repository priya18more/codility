
A = [0,1,0,1,1]

def passingCars(A):
    '''
    brute solution
    '''
    N = len(A)
    Counter = 0
    if A:
        if N == 1:
            return 0
        if N > 1:
            for i in range(len(A)):
                if A[i] == 0:
                    sumA = sum(A[i:])
                    if sumA > 0:
                        Counter += sumA
                    sumA = 0
    return Counter

def passingCars1(A):
    '''
    optimize solution
    '''
    N = len(A)
    totalSum = sum(A)
    Counter = 0
    SL = 0
    if A:
        if N == 1:
            return 0
        if N > 1:
            for i in range(N):
                SL += A[i]
                if A[i] == 0:
                    Counter += (totalSum - SL)
    if Counter > 1000000000:
        return -1
    else:
        return Counter

def passingCars2(A):
    '''
    with sufix sum solution
    '''
    sufix_sum = [0] * (len(A) + 1)
    counter = 0
    for i in range(len(A) - 1, -1, -1):
        sufix_sum[i] = A[i] + sufix_sum[i + 1]
        if A[i] == 0:
            counter += sufix_sum[i]
        if counter > 1000000000:
            return -1
    return counter

def passingCars3(A):
    '''
    prefix sum solution
    '''
    prefix_sum = [0] * (len(A) + 1)
    counter = 0
    for i in range(len(A)):
        prefix_sum[i + 1] = A[i] + prefix_sum[i]

    for i in range(len(A)):
        if A[i] == 0:
            diff = prefix_sum[-1] - prefix_sum[i + 1]
            counter += diff
        if counter > 1000000000:
            return -1

    return counter

print(passingCars(A))
print(passingCars1(A))
print(passingCars2(A))
print(passingCars3(A))