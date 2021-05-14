X = int(input())
stage = 1
while X > stage:
    X -= stage
    stage += 1

if(stage%2 == 1):
    x = stage+1 - X
    y = stage+1 - x
    print("{}/{}".format(x, y))
else:
    x = stage+1 - X
    y = stage+1 - x
    print("{}/{}".format(y, x))
