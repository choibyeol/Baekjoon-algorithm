# 모듈을 사용하지 않는 풀이
import sys
input = sys.stdin.readline

def make_comb(arr, comb, s):
    cnt = 0
    for front in arr:
        for end in list(comb):
            comb.append(front+end)
            if comb[-1] == s:
                cnt += 1
    return cnt

n, s = map(int,input().split())
comb = [0]
cnt = make_comb([*map(int, input().split())], comb, s)
print(cnt)

# 파이썬 itertools를 사용한 풀이
'''
from itertools import combinations as cb
import sys
input=sys.stdin.readline


if __name__ == "__main__":
    cnt = 0
    n, s = map(int, input().split())
    arr = [*map(int, input().split())]
    
    for i in range(1, n + 1):
        for combination in cb(arr,i):
            if sum(combination) == s:
                cnt += 1

    print(cnt)
'''
