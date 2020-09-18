def d(n):
    result = n
    n = str(n)
    for i in range(0, len(n)):
        result += int(n[i])
    return result

listN = []

for i in range(1, 10001):
    listN.append(int(i))

for i in range(1, 10001):
    if d(i) in listN:
        listN[listN.index(d(i))] = 0
              
for i in range(0, 10000):
    if(listN[i] != 0):
        print(listN[i])
