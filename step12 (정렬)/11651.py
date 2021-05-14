import sys
input = sys.stdin.readline

N = int(input())
listxy = []

for i in range(N):
    x, y = map(int, input().split())
    listxy.append([y, x])

listxy.sort()

for i in listxy:
    print(i[1], i[0])
