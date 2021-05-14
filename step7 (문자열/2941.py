alphac = ['c=','c-','dz=','d-','lj','nj','s=','z=']
A = input()
finda = 0

for i in alphac:
    finda += A.count(i)

print(len(A) - finda)
