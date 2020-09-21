def star3(S):
    matrix = []
    for i in range(3 * len(S)):
        if i // len(S) == 1:
            matrix.append(S[i % len(S)] + " "*len(S) + S[i % len(S)])
        else:
            matrix.append(S[i % len(S)] * 3)
    return list(matrix)
    
star = ['***', '* *', '***']

N = int(input())
k = 1
while N != 3:
    N = int(N/3)
    k += 1

for i in range(k-1):
    star = star3(star)
for i in star:
    print(i)

'''
def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))

64ms 걸리는 풀이 나중에 이해하기!
'''