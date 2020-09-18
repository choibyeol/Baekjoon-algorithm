A, B, V = map(int, input().split())
if(int((V-A)%(A-B)) == 0):
    print(int((V-A)/(A-B)+1))
else:
    print(int((V-A)/(A-B)+2))
