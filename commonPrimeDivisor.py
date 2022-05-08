A = [15,10,3]
B = [75,30,5]

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

def comPrimeDivisor(A, B):
    l = len(A)
    count = 0
    for i in range(l):
        a = A[i]
        b = B[i]
        D = find_gcd(a,b)
        while(find_gcd(a, D) != 1):
            a /= find_gcd(a, D)
        while(find_gcd(b, D) != 1):
            b /= find_gcd(b, D)
        if (a == 1 and b == 1):
            count+=1
    return count

print(comPrimeDivisor(A, B))