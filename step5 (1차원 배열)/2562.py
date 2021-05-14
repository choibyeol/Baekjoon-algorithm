listN = []
maxN = 0
for i in range(0,9):
    N = int(input())
    listN.append(N)
    if(maxN < N):
        maxN = N
print(maxN)
print(listN.index(maxN)+1)
