import sys

N, M = map(int, sys.stdin.readline().split())
listM = []
listM = sys.stdin.readline().split()
listM = list(map(int, listM))
listM.sort()
Max = listM[0] + listM[1] + listM[2]
for i in listM:
    for j in listM:
        if i == j:
            continue
        for k in listM:
            if(k == i or k == j):
                continue
            if(Max <= i+j+k <= M):
                Max = i+j+k
print(Max)
