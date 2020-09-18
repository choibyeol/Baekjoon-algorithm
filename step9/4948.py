import math

N = 123456 * 2 + 1
listP = [2]
for i in range(3, N):
    if i % 2 == 0:
        continue
    n = int(math.sqrt(i))
    isPrime = 1
    for j in range(2, n+1):
        if i % j == 0:
            isPrime = 0
            break
    if isPrime:
        listP.append(i)

while(True):
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in listP:
        if n < i <= n*2:
            count += 1
    print(count)
