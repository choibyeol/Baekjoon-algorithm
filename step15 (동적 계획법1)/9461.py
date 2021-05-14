import sys
input = sys.stdin.readline

PN = [0 for i in range(101)]
PN[1] = 1
PN[2] = 1
PN[3] = 1

for i in range(0, 98):
    PN[i+3] = PN[i] + PN[i+1]

T = int(input())

for i in range(T):
    N = int(input())
    print(PN[N])
