def isgroup(s):
    if(len(s) == len(set(s))):
        return 1
    else:
        for i in set(s):
            if(s.count(i) > 1):
                for j in range(s.find(i), s.find(i)+s.count(i)-1): 
                    if(s[j] != s[j+1]):
                        return 0
        return 1

N = int(input())
sumg = 0

for i in range(N):
    G = input()
    sumg += isgroup(G)

print(sumg)
