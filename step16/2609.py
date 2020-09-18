import sys
input = sys.stdin.readline

N, M = map(int, input().split())
GCD = 0 # 최대 공약수
LCM = 0 # 최소 공배수

cnt = 1
while(cnt != min(N, M)+1):
    if(N % cnt == 0 and M % cnt == 0):
        GCD = cnt
    cnt += 1

sN = N
sM = M
while(sN != sM):
    if sN < sM:
        sN += N
    else:
        sM += M
LCM = sN
print(GCD)
print(LCM)
