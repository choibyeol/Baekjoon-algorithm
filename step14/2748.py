import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n+1)]
arr[1] = 1

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])

# 재귀로 풀면 중복 연산 때문에 시간 초과
# DP로 풀 때는 값을 array에 저장하기 떄문에 중복되는 연산을 하지 않고
# 바로 답을 가지고 올 수 있기 때문에 더 빠르게 문제를 풀 수 있다.
