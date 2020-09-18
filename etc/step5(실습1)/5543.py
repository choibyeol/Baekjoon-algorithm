minburger = 3000
mindrinks = 3000
for i in range(1,6):
    n = int(input())
    if(i < 4):
        if(minburger > n):
            minburger = n
    else:
        if(mindrinks > n):
            mindrinks = n
print((minburger+mindrinks)-50)
