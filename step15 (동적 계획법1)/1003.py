import sys
input = sys.stdin.readline

cnt0 = [1, 0, 1]
cnt1 = [0, 1, 1]

def cnt_fibo(N):
    length = len(cnt0)
    if length <= N:
        for i in range(length, N+1):
            cnt0.append(cnt0[i-1] + cnt0[i-2])
            cnt1.append(cnt1[i-1] + cnt1[i-2])
    print("%d %d" % (cnt0[N], cnt1[N]))

T = int(input())

for i in range(T):
    N = int(input())
    cnt_fibo(N)
