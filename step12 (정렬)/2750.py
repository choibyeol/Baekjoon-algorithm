import sys
N = int(sys.stdin.readline())
listn = []
for i in range(N):
    n = int(sys.stdin.readline())
    listn.append(n)
listn.sort()
for i in listn:
    print(i)
