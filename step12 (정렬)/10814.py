import sys
input = sys.stdin.readline

N = int(input())
listN = []

for i in range(N):
    a, n = input().split()
    listN.append([a, n])

listN.sort(key=lambda listN: int(listN[0]))

for i in range(N):
    print(listN[i][0], listN[i][1])
