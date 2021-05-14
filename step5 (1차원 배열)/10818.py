N = int(input())
listN = []
listN2 = []
elements = input()
listN = elements.split(" ")

for i in range(0,N):
    listN2.append(int(listN[i]))

print("%d %d" % (min(listN2), max(listN2)))

'''
a = int(input())
b = input()
b = list(map(int, b.split(' ')))

print(str(min(b)) + ' ' + str(max(b)))

또는

N = int(input())
ls = list(map(int, input().split()))
print(min(ls),max(ls))

list(map(int, input().split())) 기억하자!
'''
