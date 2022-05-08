
N = 5
A = [3,4,4,6,1,4,4]

def maxCounter(N,A):
    R = [0]*N
    maxC = 0
    baseV = 0
    if A:
        for i in range(len(A)):
            if A[i] <= N:
                R[A[i]-1] = max(baseV,R[A[i]-1]) + 1
                print(R)
                maxC = max(maxC,R[A[i]-1])
                print(maxC)
            else:
                baseV = maxC
                print(baseV)
        for i in range(0, len(R)):
            if R[i] < baseV:
                R[i] = baseV
    return R

def maxCounter2(N,A):
    counters = [0] * N
    start_line = 0
    current_max = 0

    for i in A:
        x = i - 1
        if i > N:
            start_line = current_max
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1

        if i <= N and counters[x] > current_max:
            current_max = counters[x]

    for i in range(len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line

    return counters


print(maxCounter(N,A))
print(maxCounter2(N,A))