import sys
input = sys.stdin.readline

A = int(input())
listA = list(map(int, input().split()))
dp = [0 for i in range(A)]

for i in range(A):
    for j in range(i):
        if listA[i] > listA[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
