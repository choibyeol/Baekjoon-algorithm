T = int(input())
for i in range(T):
    OX = input()
    totalsum = 0
    sumOX = 0
    for j in range(len(OX)):
        if OX[j] == 'O':
            sumOX += 1
        else:
            sumOX = 0
        totalsum += sumOX
    print(totalsum)

