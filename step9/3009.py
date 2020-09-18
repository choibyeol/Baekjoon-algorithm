listx = []
listy = []

for i in range(3):
    x, y = map(int, input().split())
    listx.append(x)
    listy.append(y)

setx = set(listx)
sety = set(listy)
setx = list(setx)
sety = list(sety)

X1 = setx[0]
X2 = setx[1]
Y1 = sety[0]
Y2 = sety[1]

if listx.count(X1) == 1:
    X = X1
else:
    X = X2
if listy.count(Y1) == 1:
    Y = Y1
else:
    Y = Y2

print("%d %d" % (X, Y))
