S = "([)()]"

def brackest(S):
    if(len(S) == 0):
        return 1
    V = []
    C = {'[': +1, ']': -1, '(': +2, ')': -2, '{': +3, '}': -3}

    for i in range(len(S)):
        if i == 0 and C[S[i]] < 0:
            return 0
        elif C[S[i]] < 0 and len(V) == 0:
            return 0
        elif C[S[i]] < 0 and C[S[i]] != -V[-1]:
            return 0
        elif C[S[i]] < 0:
            print(S[i])
            V.pop()
        else:
            print(V)
            V.append(C[S[i]])
    if len(V) == 0 :
        return 1
    else:
        return 0

def brackets2(S):
    valid = True
    stack = []

    for c in S:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c == ')':
            valid = False if not stack or stack.pop() != '(' else valid
        elif c == ']':
            valid = False if not stack or stack.pop() != '[' else valid
        elif c == '}':
            valid = False if not stack or stack.pop() != '{' else valid
    return 1 if valid and not stack else 0

print(brackets2(S))

print(brackest(S))

