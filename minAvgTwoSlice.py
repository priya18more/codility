
A = [4,2,2,5,1,5,8]

def minAvgTwoSlice(A):
    '''
    performance : 40, correctness : 40
    '''
    mv = max(A)*2
    mi = 0
    for i in range(0, len(A)-2):
        v1 = (A[i] + A[i+1] + A[i+2])/3
        v2 = (A[i] + A[i+1])/2
        if mv > v1 or mv > v2:
            mv = min(v1,v2)
            mi = i
        if mv > (A[-1] + A[-2])/2:
            return len(A)- 2
    return mi

def minAvgTwoslice1(A):
    min_avg = (A[0] + A[1])/2
    min_inx = 0
    for i in range(0, len(A)-2):
        v1 = (A[i] + A[i + 1] + A[i + 2]) / 3
        v2 = (A[i] + A[i + 1]) / 2
        v3 = A[-2] + A[-1] / 2
        if min_avg > v1 or min_avg > v2:
            min_inx = i
            min_avg = min(v1,v2)
        if min_avg > v3:
            min_inx = len(A) - 2
            min_avg = v3
    return min_inx

def minAvgtwoSlice2(A):
    '''
    Performance, correctness, task : 100%
    '''
    indexOfmin2 = -1
    minSumof2 = 1000000
    N = len(A)
    indexOfmin3 = -1
    minSumof3 = 1000000

    for i in range(N-1):
        val1 = A[i]
        val2 = A[i + 1]
        sumOf2 = val1 + val2
        if sumOf2 < minSumof2:
            minSumof2 = sumOf2
            indexOfmin2 = i

        if i < N -2:
            val1 = A[i]
            val2 = A[i+1]
            val3 = A[i+2]
            sumOf3 = val1 + val2 + val3
            if sumOf3 < minSumof3:
                minSumof3 = sumOf3
                indexOfmin3 = i

    if indexOfmin3 == -1:
        return 0

    minSumof2 /= 2
    minSumof3 /= 3
    if minSumof2 < minSumof3:
        return indexOfmin2
    elif minSumof3 < minSumof2:
        return indexOfmin3
    else:
        return min(indexOfmin2,indexOfmin3)



#print(minAvgTwoSlice(A))
#print(minAvgTwoslice1(A))
print(minAvgtwoSlice2(A))