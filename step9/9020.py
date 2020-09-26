import sys
input = sys.stdin.readline

def prime_list(n):
    s = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if s[i] == True:
            for j in range(i+i, n, i):
                s[j] = False
    return [i for i in range(2, n) if s[i] == True]
# 에라토스테네스의 체로 소수 찾기

def sosu(n):
    li = prime_list(n)
    idx = max([i for i in range(len(li)) if li[i] <= n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            if (li[i]+li[j]) == n:
                return [li[i], li[j]]

T = int(input())

for _ in range(T):
    n = int(input())
    print(" ".join(map(str, sosu(n))))
