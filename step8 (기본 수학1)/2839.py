N = int(input())
Count = 0
sum5 = 0
while True:
    if(N % 5 == 0):
        sum5 = int(N/5)
        Count += sum5
        break
    else:
        N -= 3
        Count += 1
    if(N == 0):
        break
    elif(N < 0):
        Count = -1
        break
        
print(Count)    
