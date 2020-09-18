N = int(input())
if(N == 1):
    print('*')
else:
    for i in range(1, N+1):
        if(N%2 == 1):
            print('*' + ' *'*(int(N/2)))
            print(' *' + ' *'*(int(N/2-1)))
        else:
            print('*' + ' *'*(int(N/2)-1))
            print(' *' + ' *'*(int(N/2)-1))
