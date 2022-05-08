import math
X = 1
Y = 5
D = 2

def FrogImp(X,Y,D):
    if X < Y and X > 0 and Y > 0:
        noOfJumps = math.ceil((Y - X) / D)
    else:
        return 0
    if ((D * noOfJumps)+X) >= Y:
        return noOfJumps



print(FrogImp(X,Y,D))