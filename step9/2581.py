def findN(N):
    divisor = 1
    pnum = 0
    for j in range(N):
        if(N % divisor == 0):
            pnum += 1
        divisor += 1
    if(pnum == 2):
        return 1

M = int(input())
N = int(input())
listP = []

for i in range(M, N+1):
    if(findN(i) == 1):
        listP.append(i)

if(len(listP) == 0):
    print(-1)
else:
    print(sum(listP))
    print(listP[0])
