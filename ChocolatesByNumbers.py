N = 10
M = 4

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

def chocByNumber(N, M):
    return N // find_gcd(N, M)


print(chocByNumber(N, M))

