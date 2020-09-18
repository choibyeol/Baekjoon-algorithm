N = int(input())
j = 0
for i in range(2*N-1, 0, -2):
    print(' '*j + '*'*i)
    j += 1
k = j-2
for i in range(3, 2*N, 2):
    print(' '*k + '*'*i)
    k -= 1
