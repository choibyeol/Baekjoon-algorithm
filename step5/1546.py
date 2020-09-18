N = int(input())
listN = list(map(int, input().split()))
sumN = 0
maxN = max(listN)
for i in range(N):
        sumN += listN[i] / maxN * 100
print(sumN / N)
