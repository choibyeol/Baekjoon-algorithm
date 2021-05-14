T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    people = [ i for i in range(1, n+1)]

    for __ in range(k):
        for j in range(1,n):
            people[j] += people[j-1]
    print(people[-1])

'''
def sumkn(k, n):
    result = 0
    if(k == 0):
        for i in range(1, n+1):
            result += i
    else:
        for i in range(1, n+1):
            result += sumkn(k-1, i)
    return result

#'int' object is not callable 변수와 함수의 이름이 같을 때 발생

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(sumkn(k, n))
   ''' 
