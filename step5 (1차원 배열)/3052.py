listN = []
for i in range(10):
    N = int(input())
    listN.append(N%42)
print(len(set(listN)))
