def X(n):
    n = str(n)
    if(len(n) == 1 or len(n) == 2):
        return 1
    else:
        result = 1
        differ = int(n[1]) - int(n[0])
        for i in range(2, len(n)):
            if(differ != int(n[i]) - int(n[i-1])):
                result = 0
        return result

N = int(input())
sumX  = 0
for i in range(1, N+1):
    if(X(i) == 1):
        sumX += 1
print(sumX)
