S = input()
alphabet = []
for i in range(0,26):
    alphabet.append(-1)
for i in range(0, len(S)):
    if(alphabet[ord(S[i])-97] == -1):
        alphabet[ord(S[i])-97] = i  # ord(a)는 아스키코드 97
for i in range(0, len(alphabet)-1):
    print(alphabet[i], end =" ")
print(alphabet[25])
