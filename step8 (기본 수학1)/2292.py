N = int(input())
count = 1
sumN = 1
sum6 = 6
if(N == 1):
    print(1)
else:
    while True:
        sumN += sum6
        count += 1
        if(N <= sumN):
            print(count)
            break
        sum6 += 6
