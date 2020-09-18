import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(X, Y):
    global listMN, M, N
    for i in range(4):
        XX, YY = X + dx[i], Y + dy[i]
        if XX < 0 or XX == M or YY < 0 or YY == N:
            continue
        if listMN[XX][YY] == 1:
            listMN[XX][YY] = 0
            dfs(XX, YY)

for _ in range(T):
    M, N, K = map(int, input().split())
    listMN = [[0 for i in range(N)] for j in range(M)]
    jirung = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        listMN[X][Y] = 1
    for i in range(M):
        for j in range(N):
            if listMN[i][j] == 1:
                dfs(i, j)
                jirung += 1
    print(jirung)
