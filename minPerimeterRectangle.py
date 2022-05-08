import math

N = 30

def minPeremeter(N):
    i = int(math.ceil(math.sqrt(N)))

    while i >= 1:
        if (N/i) % 1 == 0:
            return int(i*2 + ((N/i) * 2))
        i -= 1
    return 0


print(minPeremeter(N))
