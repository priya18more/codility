
S = "((())())"

def Nesting(S):
    counter = 0
    if len(S) == 0:
        return 1
    if S :
        for i in range(len(S)):
            if S[i] == '(':
                counter += 1
            elif S[i] == ')':
                counter -= 1
            if counter < 0:
                return 0
        if counter != 0:
            return 0
        else:
            return 1


print(Nesting(S))