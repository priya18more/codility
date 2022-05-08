A = [-5, -3, -1, 0, 3, 6]

def absDistinct(A):
    A = [a*a for a in A]
    A = list(set(A))
    return len(A)

def absDistinct2(A):
    count = 1
    index_head = 0
    index_tail = len(A) - 1
    mymax = max(abs(A[0]),abs(A[-1]))
    while index_head <= index_tail:
        head = abs(A[index_head])
        tail = abs(A[index_tail])
        if head == mymax:
            index_head += 1
            continue
        if tail == mymax:
            index_tail -= 1
            continue
        if head >= tail:
            mymax = head
            index_head += 1
        else:
            mymax = tail
            index_tail -= 1
        count += 1
    return count



print(absDistinct(A))
print(absDistinct2(A))