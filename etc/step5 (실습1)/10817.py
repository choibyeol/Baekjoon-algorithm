A, B, C = map(int, input().split())
sum = A + B + C
print(sum - max(A,B,C) - min(A,B,C))
