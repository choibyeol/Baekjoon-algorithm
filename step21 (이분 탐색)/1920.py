import sys
input = sys.stdin.readline
n = int(input())
N = sorted(map(int, input().split()))
m = int(input())
M = map(int, input().split())

def binary(i, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if i == N[m]:
        return 1
    elif i < N[m]:
        return binary(i, N, start, m-1)
    else:
        return binary(i, N, m+1, end)

for i in M:
    start = 0
    end = len(N)-1
    print(binary(i, N, start, end))


''' 시간초과
import sys
input = sys.stdin.readline

N = int(input())
NA = input().split()
M = int(input())
MA = input().split()

for i in MA:
    init = 0
    for j in NA:
        if i == j:
            init = 1
        if j == NA[-1]:
            if init == 1:
                print(1)
            else:
                print(0)
'''
