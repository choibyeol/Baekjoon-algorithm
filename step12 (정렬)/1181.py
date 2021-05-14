N = int(input())
listN = []
for i in range(N):
    listN.append(input())

listN = set(listN)
listN = list(listN)
listN.sort()
listN.sort(key=len)
for i in listN:
    print(i)
