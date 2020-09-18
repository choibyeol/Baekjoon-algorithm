A, B = input().split()
rA = rB = ''

for i in range(2, -1, -1):
    rA += A[i]
    rB += B[i]
    
rA = int(rA)
rB = int(rB)

if(rA > rB):
    print(rA)
else:
    print(rB)
