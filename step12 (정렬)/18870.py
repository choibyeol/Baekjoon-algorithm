N = int(input())
listN = list(map(int, input().split()))
sN = list(sorted(set(listN)))
D = {}
for i in range(len(sN)):
    D[sN[i]] = i
for i in listN:
    print(D[i], end=" ")
