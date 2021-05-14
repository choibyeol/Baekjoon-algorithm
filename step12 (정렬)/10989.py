import sys
N = int(sys.stdin.readline()) # input()으로 입력 받으면 메모리 초과
b = [0] * 10001
for i in range(N):
    b[int(sys.stdin.readline())] += 1 # 각 숫자의 개수
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]): # 숫자의 수 만큼 출
            print(i)
