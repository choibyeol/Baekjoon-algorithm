import sys
input = sys.stdin.readline

def isTrue(x):
    for i in range(x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x-i:
            return False
    return True

def dfs(x):
    global result
    
    if x == N:
        result += 1
    else:
        for i in range(N):
            s[x] = i
            if isTrue(x):
                dfs(x + 1)
                
N = int(input())
s = [0] * N
result = 0
dfs(0)
print(result)

// 파이썬으로 하면 시간 초과^^!! 난 모르겠다.

'''
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])

// 정답으로 뜨긴 하지만......
'''
