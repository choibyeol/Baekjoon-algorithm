import sys
import operator
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
inc = [0 for i in range(N)]
dec = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and inc[i] < inc[j]:
            inc[i] = inc[j]
    inc[i] += 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j] and dec[i] < dec[j]:
            dec[i] = dec[j]
    dec[i] += 1

print(str(max(map(operator.add, inc, dec))-1))
