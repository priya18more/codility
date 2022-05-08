
A = [1,2,3,4,1,1,3]
K = 4

def tieRopes(A,K):
    ropeLenght = 0
    count = 0
    for length in A:
        ropeLenght += length
        if ropeLenght >= K:
            count += 1
            ropeLenght = 0
    return count

print(tieRopes(A,K))
