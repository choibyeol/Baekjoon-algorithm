import sys
input = sys.stdin.readline

arr = [0 for i in range(301)]
dp = [0 for i in range(301)]

N = int(input())

for i in range(N):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])

print(dp[N-1])
