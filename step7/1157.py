def countalpha(S, a):
    return S.count(a)

S = input()
S = S.upper()
Sset = set(S)
findmax = 0
findalpha = ''
listcount = []

for i in Sset:
    if(findmax <= countalpha(S, i)):
        findmax = countalpha(S,i)
        findalpha = i
    listcount.append(countalpha(S,i))

if(listcount.count(findmax) > 1):
    print('?')
else:
    print(findalpha)
