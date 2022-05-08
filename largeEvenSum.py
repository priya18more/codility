'''
write function that takes array A of N positive intergers and positive int K, returns largest even sum of K elements
'''


A = [2,4,3,5,6,8,6,9,7,4,2,6,9,6,4,32,7,32,4,6]
K = 3

def largeEvenSum(A,K):
    evenArr = []
    oddArr = []
    A = sorted(A)
    if len(A) < K:
        return -1

    for i in A:
        if i % 2 == 0:
            evenArr.append(i)
        else:
            oddArr.append(i)

    print(oddArr)
    print(evenArr)

    maxSum = 0
    if K % 2 != 0:
        if K <= len(evenArr):
            evenEleSum = sum(evenArr[-K:])
            return evenEleSum
        else:
            return -1
    else:
        if K <= len(evenArr) and K <= len(oddArr):
            evenEleSum = sum(evenArr[-K:])
            oddEleSum = sum(oddArr[-K:])
            maxSum = max(oddEleSum, evenEleSum)
            return maxSum
        elif K <= len(evenArr) and K > len(oddArr):
            return sum(evenArr[-K:])
        elif K <= len(oddArr) and K > len(evenArr):
            return sum(oddArr[-K:])
        else:
            return -1


print(largeEvenSum(A,K))