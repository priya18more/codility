
H = [8,8,5,7,9,8,7,4,8]

def stoneWall(H):
    last = 0
    counter = 0
    Stone =[]
    for i in range(len(H)):
        if H[i] > last:
            last = H[i]
            counter += 1
            Stone.append(H[i])
        elif H[i] < last:
            while len(Stone) != 0 and H[i] < Stone[-1]:
                Stone.pop()
            if len(Stone) == 0 or H[i] != Stone[-1]:
                counter += 1
                Stone.append(H[i])
            last = H[i]
    return counter

def stoneWall2(H):
    blockcounter = 0
    stack = []

    for h in H:
        while len(stack) != 0 and stack[-1] > h:
            stack.pop()
        if len(stack) != 0 and stack[-1] == h:
            '''no change'''
        else:
            stack.append(h)
            blockcounter += 1
    return blockcounter

print(stoneWall(H))

print(stoneWall2(H))