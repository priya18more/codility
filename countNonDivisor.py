A = [3,1,2,3,6]

def nonDivisor(A):
    m = max(A)
    R = []
    nonDivUni = {}
    counts = [0] * (m+1)

    for a in A:
        counts[a] += 1

    uniA = set(A)
    for a in uniA:
        print("-----a----")
        print(a)
        print("-----------")
        s = 0
        print("-----sq a-----")
        print(int(a**0.5))
        print("--------------")
        for j in range(1,int(a**0.5)+1):
            print("-----a mod j and j------")
            print(a%j)
            print(j)
            print("--------------")
            if a % j == 0:
                s+= counts[j]
                print("----s and counts----")
                print(s)
                print(counts)
                print(counts[j])
                print("---------")
                if(int(a/j) != j):
                    s+= counts[int(a/j)]
                    print("-----inner s and counts-------")
                    print(s)
                    print(counts)
                    print(counts[int(a / j)])
                    print("------------------------------")
        nonDivUni[a] = len(A) - s
        print("-------non div---------")
        print(nonDivUni)
        print("----------------------")

    for a in A:
        R.append(nonDivUni[a])

    return R



print(nonDivisor(A))