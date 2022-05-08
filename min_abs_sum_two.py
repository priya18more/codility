A = [-8,4,5,-10,3]


def min_abs_sum_two(A):
    min_abs_sum = 2000000000
    A = sorted(A)
    head = 0
    tail = len(A) -1

    while head <= tail:
        sum_two = A[head] + A[tail]
        min_abs_sum = min(min_abs_sum,abs(sum_two))
        if sum_two < 0:
            head += 1
        else:
            tail -= 1
    return min_abs_sum

print(min_abs_sum_two(A))