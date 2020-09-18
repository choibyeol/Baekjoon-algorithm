T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if(N % H == 0):
        Y = H
    else:
        Y = N % H
    if(N%H == 0):
        X = int(N/H)
    else:
        X = int(N/H) + 1
    if(X < 10):
        print(str(Y)+'0'+str(X))
    else:
        print(str(Y)+str(X))
