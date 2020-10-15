import sys
from collections import Counter
input = sys.stdin.readline

def mostfinder(numbers):
    cnt = Counter(numbers)
    order = cnt.most_common()
    maxcnt = order[0][1]
    maxn = order[0][0]
    if order[1][1] == maxcnt:
        maxn = order[1][0]
    return maxn

N = int(input())
listN = []
cnt = 0
for i in range(N):
    listN.append(int(input()))

listN.sort()
print(round(sum(listN) / N))
print(listN[int(N/2)])
if N == 1:
    print(listN[0])
else:
    print(mostfinder(listN))
print(max(listN) - min(listN))
