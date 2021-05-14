import sys
input = sys.stdin.readline

N = int(input())
listxy = []

for i in range(N):
    x, y = map(int, input().split())
    listxy.append([x, y])

listxy.sort()

for i in listxy:
    print(i[0], i[1])
