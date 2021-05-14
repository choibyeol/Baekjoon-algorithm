sum = 0
for i in range(1,6):
    n = int(input())
    if(n >= 40):
        sum += n
    else:
        sum += 40
print(int(sum/5))
