A = [2,4,5,1,3]

def missingInteger(A):
    '''
    solution 1: only for positive values
    '''
    A = sorted(A)
    print(A)
    if A :
        for count,element in enumerate(A,start=1):
            if count != element:
                print(count, element)
                return count
        return len(A) + 1
    else:
        return 1

def missingInteger1(A):
    '''
    solution 2:
    '''
    actualSum = 0
    for number in A:
        actualSum += number

    maxNum = len(A) + 1
    expectedSum = maxNum * (maxNum + 1) // 2

    missingPerm = expectedSum - actualSum
    return missingPerm

print(missingInteger(A))
print(missingInteger1(A))