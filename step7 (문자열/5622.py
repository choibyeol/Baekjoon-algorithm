alphabetlist = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
A = input()
time = 0

for alpha in alphabetlist:
    for i in alpha:
        for x in A:
            if i == x:
                time += alphabetlist.index(alpha)+3
                
print(time)

'''
A = input()
sumA = 0

for i in range(len(A)):
    if(A[i] == 'A' or A[i] == 'B' or A[i] == 'C'):
        sumA += 3
    elif(A[i] == 'D' or A[i] == 'E' or A[i] == 'F'):
        sumA += 4
    elif(A[i] == 'G' or A[i] == 'H' or A[i] == 'I'):
        sumA += 5
    elif(A[i] == 'J' or A[i] == 'K' or A[i] == 'L'):
        sumA += 6
    elif(A[i] == 'M' or A[i] == 'N' or A[i] == 'O'):
        sumA += 7
    elif(A[i] == 'P' or A[i] == 'Q' or A[i] == 'R' or A[i] == 'S'):
        sumA += 8
    elif(A[i] == 'T' or A[i] == 'U' or A[i] == 'V'):
        sumA += 9
    elif(A[i] == 'W' or A[i] == 'X' or A[i] == 'Y' or A[i] == 'Z'):
        sumA += 10
        
print(sumA)

//
부끄러운 첫 번째 제출 코드
어차피 방법은 똑같지만 무식하게 if문 안써도 됐음 ㅠㅠ
아무리 생각해도 이건 아닌 것 같아서 다시 풀었다.....
코드가 짧아지긴 했는데 이것도 for문이 너무 많이 돈다..
더 좋은 코드는 없나...? 어렵다 어려워
'''


