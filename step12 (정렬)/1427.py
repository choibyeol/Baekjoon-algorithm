N = input()
listN = []
for i in range(0, len(N)):
    listN.append(int(N[i]))
listN.sort(reverse=True)
for i in range (0, len(listN)):
    print(listN[i], end="")

# print(''.join(sorted(input())[::-1]))
# 한줄로 되네..
