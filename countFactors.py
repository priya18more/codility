import math
N = 24

def FactorCount(N):
    i = 1
    factors = 0
    sqN = math.sqrt(N)
    while i <= sqN:
        if N % i == 0:
            if i < sqN:
                factors+=2
            else:
                factors+= 1
        i += 1
    return factors

print(FactorCount(N))