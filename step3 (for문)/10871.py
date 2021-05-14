N, X = map(int, input().split())
n = input().split()
for i in range(0, N):
    if(int(n[i]) < X):
        print(n[i], end = " ")
