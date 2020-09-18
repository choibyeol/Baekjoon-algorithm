N = int(input())
listN = input().split()
countN = 0
for i in listN:
    divisor = 1
    pnum = 0
    for j in range(int(i)):
        if(int(i) % divisor == 0):
            pnum += 1
        divisor += 1
    if(pnum == 2):
        countN += 1
print(countN)
