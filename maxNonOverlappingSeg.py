A = [1,3,7,9,9]
B = [5,6,8,9,10]

def nonOverlappingSeg(A,B):
    last_end_segment = -1
    chosen_count = 0
    for i in range(len(A)):
        if A[i] > last_end_segment:
            chosen_count += 1
            last_end_segment = B[i]
    return chosen_count



print(nonOverlappingSeg(A,B))