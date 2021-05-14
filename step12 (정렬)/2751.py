N = int(input())
listn = []
for i in range(N):
    listn.append(int(input()))

listn.sort()
for i in range(len(listn)):
    print(listn[i])

# pypy3으로 제출하거나

'''
import sys
input()
for i in sorted(map(int,list(sys.stdin))):
	print(i)
'''
