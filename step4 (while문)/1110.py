N = input()
N2 = N
cycle = 0
sumN = 0
while(1):
    if(int(N2) < 10):
        if(len(N2) == 1):
            N2 = N2+N2
        else:
            N2 = N2[1] + N2[1]
    else:
        sumN = int(N2[0]) + int(N2[1])
        if(int(sumN) < 10):
            sumN = str(sumN)
            N2 = N2[1] + sumN[0]
        else:
            sumN = str(sumN)
            N2 = N2[1] + sumN[1]
    cycle += 1
    if(int(N) == int(N2)):
        break
print(cycle)

'''
a=int(input())
b=a
count = 0

while True:
    count+=1
    a=(a%10*10)+(a//10+a%10)%10
    if a==b:
        break
        
print(count)

코드를 짧게 짜는 연습을 하자.....
'''
