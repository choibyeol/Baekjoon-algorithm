import sys
stack = []
N = int(sys.stdin.readline())
X = []
for i in range(N):
    X.clear()
    X = sys.stdin.readline().split()
    if(X[0] == 'push'):
        stack.append(int(X[1]))
    elif(X[0] == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
    elif(X[0] == 'size'):
        print(len(stack))
    elif(X[0] == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(X[0] == 'pop'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
