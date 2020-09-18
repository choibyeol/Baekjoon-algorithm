X = int(input())
M = 64
sumX = 0
count = 0
while(X != sumX):
    if(sumX + M <= X):
        sumX += M
        count += 1
    M = int(M/2)
print(count)

''' print(bin(int(input()))[2:].count('1'))
간단히 한줄로도 작성 가능!
bin() 이진수로 바꿔주는 함수.
bin(n)[2:] 하면 앞에 0b 제거해준다. 따라서 0b 제거해주고
count로 1 체크해주면 끝!
'''
