import sys
input = sys.stdin.readline

xl = []
yl = []

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)

dunchi = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if j == i:
            continue
        if xl[i] < xl[j] and yl[i] < yl[j]:
            cnt += 1
    dunchi.append(cnt)

for i in range(N-1):
    print(dunchi[i], end=" ")
print(dunchi[-1])
