
A = [4,3,4,4,4,2]

def equiLeader(A):
    dominator = 0
    dominatorCount = 0
    N = len(A)
    mapDcounter = {}

    for i in range(N):
        a = A[i]
        if a in mapDcounter:
            mapDcounter[a] += 1
        else:
            mapDcounter[a] = 1
        if (mapDcounter.get(a) > int(N/2)):
            dominator = a
            dominatorCount = mapDcounter.get(a)

    leadersInRightSide = dominatorCount
    countRightSide = len(A)
    countLeftSide = 0
    leaderInLeftSide = 0
    eqLeader = 0

    for i in range(N):
        if A[i] == dominator:
            leadersInRightSide -= 1
            leaderInLeftSide += 1
        countLeftSide += 1
        countRightSide -= 1

        if leaderInLeftSide > int(countLeftSide/2):
            if leadersInRightSide > int(countRightSide/2):
                eqLeader += 1
    return eqLeader

def equiLeader2(A):
    consecutive_size = 0
    candidate = 0
    dominator = 0
    N = len(A)

    for item in A:
        if consecutive_size == 0:
            candidate = item
            consecutive_size += 1
        elif candidate == item:
            consecutive_size += 1
        else:
            consecutive_size -= 1

    dCounter = A.count(candidate)
    if dCounter > int(N/2):
        dominator = candidate

    RightSideLeader = dCounter
    RightCount = N
    LeftSideLeader = 0
    LeftCount = 0
    eCount = 0

    for i in range(N):
        a = A[i]
        if a == dominator:
            RightSideLeader -= 1
            LeftSideLeader += 1
        RightCount -= 1
        LeftCount += 1

        if LeftSideLeader > int(LeftCount/2):
            if RightSideLeader > int(RightCount/2):
                eCount += 1
    return eCount


print(equiLeader(A))
print(equiLeader2(A))