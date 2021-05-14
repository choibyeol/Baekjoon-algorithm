T = int(input())
for i in range(T):
    S = input()
    lenS = int(S[0])
    for i in range(2, len(S)):
        for j in range(0, lenS):
            print(S[i], end = "")
    print()
