P = [1,4,16]
Q = [26,10,20]
N = 26

def countSemiPrimes(N,P,Q):
    primes = [1] * (N+1)
    primes[0] = primes[1] = 0

    for i in range(2, int(N**0.5)+1):
        print(primes)
        if primes[i]:
            k=i*i
            while k<=N:
                primes[k]=0
                k+=i
                print(k)

    allSemiPrimes = [0] * (N+1)

    for i in range(0,N+1):
        for j in range(0,N+1):
            if primes[i] and primes[j] and i*j<=N:
                allSemiPrimes[i*j]=1
                print(allSemiPrimes)
            if i*j > N:
                break

    semiPrimes = [0] * len(P)
    semiPrimesCum = [0] * (N+1)
    s = 0

    for i in range(0, N+1):
        s+=allSemiPrimes[i]
        semiPrimesCum[i]=s
        print(semiPrimesCum)

    for i in range(0, len(P)):
        semiPrimes[i] = semiPrimesCum[Q[i]] - semiPrimesCum[P[i]-1]

    return semiPrimes



print(countSemiPrimes(N,P,Q))