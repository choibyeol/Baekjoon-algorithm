import sys
T = int(input())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

''' input 대신 sys.stdin.readline()을 사용할 수 있다.
A와 B를 한줄에서 입력 받기 때문에 sys.stdin.readline().split()을 통해 라인을
입력 받은 후 split 함수로 나누어 A와 B에 두 수를 넣고 int형으로 변환시킨 값을
다시 넣어주게 된다.
'''
