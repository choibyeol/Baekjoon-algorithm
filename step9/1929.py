import math

def isPrime(N):
    if N == 1:
        return False

    n = int(math.sqrt(N)) #제곱근까지만 구해보면 된다. 아니면 시간초과
    for i in range(2, n+1):
        if N % i == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i):
        print(i)
