
A = [5,4,3,2,3,-1,3,3,3]

def dominator(A):
    N = len(A)
    if N == 0:
        return -1
    elif N == 1:
        return 0
    elif N > 1:
        S = A.copy()
        S = sorted(S)
        counter = 1

        for i in range(1,N):
            if S[i] != S[i - 1]:
                counter = 1
            else:
                counter += 1
            if counter > int(N/2):
                return A.index(S[i])
        return -1

def dominator2(A):
    consecutive_size = 0
    candidate = 0

    for item in A:
        if consecutive_size == 0:
            candidate = item
            consecutive_size += 1
        elif candidate == item:
            consecutive_size += 1
        else:
            consecutive_size -= 1

    occurence = A.count(candidate)

    if occurence > (len(A) / 2):
        return A.index(candidate)
    else:
        return -1


print(dominator(A))
print(dominator2(A))