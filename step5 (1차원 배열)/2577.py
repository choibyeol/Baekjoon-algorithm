A = int(input())
B = int(input())
C = int(input())
mulABC = A * B * C
mulABC = str(mulABC)
lenABC = len(mulABC)
listABC = []
for i in range(10):
    listABC.append(0)
for i in range (0, lenABC):
    listABC[int(mulABC[i])] += 1
for i in range (10):
    print(listABC[i])
