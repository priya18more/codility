
A = [4,3,2,1,5]
B = [0,1,0,0,0]

def liveFish(A,B):
    ds = []
    counter = 0
    for i in range(len(B)):
        if B[i] == 1:
            ds.append(A[i])
        else:
            while len(ds) != 0:
                if ds[-1]>A[i] :
                    counter += 1
                    break
                elif ds[-1]<A[i]:
                    ds.pop()
                    counter +=1
    return len(A) - counter

def liveFish2(A,B):
    stack = []
    survivors = 0

    for i in range(len(A)):
        weight = A[i]
        if B[i] == 1:
            stack.append(weight)
        else:
            weightdown = stack.pop() if stack else -1
            while weightdown != -1 and weightdown < weight:
                weightdown = stack.pop() if stack else -1
            if weightdown == -1:
                survivors += 1
            else:
                stack.append(weightdown)
    return survivors + len(stack)

print(liveFish(A,B))
print(liveFish(A,B))