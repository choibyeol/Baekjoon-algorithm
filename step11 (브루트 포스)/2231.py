import sys
input = sys.stdin.readline

def findM(N):
    find = False
    iM = N
    M = str(iM)
    minM = 1000000
    while iM != 0:
        sumM = 0
        M = str(iM)
        for i in M:
            sumM += int(i)
        if(sumM + iM) == N:
            if(minM >= iM):
                minM = iM
            find = True
        if(len(str(N)) - len(M) == 2):
            break
        iM -= 1
    if(find == False):
        return 0
    return minM

N = int(input())
M = findM(N)
print(M)
