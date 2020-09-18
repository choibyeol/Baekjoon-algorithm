'''
import sys
input = sys.stdin.readline

arb = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def arb_to_rom(n):
    i = 0
    s = ""
    while i<13:
        if n>=arb[i]:
            n -= arb[i]
            s += rom[i]
            continue
        else:
            i += 1
    return s

dic = {}
for i in range(1, 4000):
    dic[arb_to_rom(i)] = i

def rom_to_arb(s):
    return dic[s]

s1 = input().rstrip()
s2 = input().rstrip()
r1 = rom_to_arb(s1)
r2 = rom_to_arb(s2)
r3 = r1+r2
s3 = arb_to_rom(r3)

print(r3)
print(s3)
'''

import sys
input = sys.stdin.readline

M = 1000; D = 500; C = 100; L = 50; X = 10; V = 5; I = 1
# V, L, D는 한 번만 사용 가능. I, X, C, M은 연속해서 세 번까지 사용 가능
IV = 4; IX = 9; XL = 40; XC = 90; CD = 400; CM = 900
# 한 번씩만 사용 가능. IV와 IX 같이 불가능. XL, XC, CD, CM 또한 같이 불가능
# 이 경우를 제외하고는 작은 숫자가 큰 숫자 왼쪽 어디에도 나올 수 X.

LA = input().rstrip() # 입력 받았을 때 \n 제거용
LB = input().rstrip()

sumA = 0 # 아라비아숫자 넣어줄 변수
sumB = 0

cnt = 0
cntI = 0 # IV, IX 카운트
cntX = 0 # XL, XC 카운트
cntC = 0 # CD, CM 카운트
for i in LA:
    if i == 'M':
        sumA += M
    elif i == 'D':
        sumA += D
    elif i == 'C':
        if cnt < len(LA)-1 and cntC == 0:
            if LA[cnt+1] == 'D':
                sumA += CD
                cntC += CD
            elif LA[cnt+1] == 'M':
                sumA += CM
                cntC += CM
            else:
                sumA += C
        else:
            sumA += C
    elif i == 'L':
        sumA += L
    elif i == 'X':
        if cnt < len(LA)-1 and cntX == 0:
            if LA[cnt+1] == 'L':
                sumA += XL
                cntX += XL
            elif LA[cnt+1] == 'C':
                sumA += XC
                cntX += XC
            else:
                sumA += X
        else:
            sumA += X
    elif i == 'V':
        sumA += V
    elif i == 'I':
        if cnt < len(LA)-1 and cntI == 0:
            if LA[cnt+1] == 'V':
                sumA += IV
                cntI += IV
            elif LA[cnt+1] == 'X':
                sumA += IX
                cntI += IX
            else:
                sumA += I
        else:
            sumA += I
    cnt += 1

if cntI == IV:
    sumA -= V
elif cntI == IX:
    sumA -= X
if cntX == XL:
    sumA -= L
elif cntX == XC:
    sumA -= C
if cntC == CD:
    sumA -= D
elif cntC == CM:
    sumA -= M


cnt = 0
cntI = 0
cntX = 0
cntC = 0
for i in LB:
    if i == 'M':
        sumB += M
    elif i == 'D':
        sumB += D
    elif i == 'C':
        if cnt < len(LB)-1 and cntC == 0:
            if LB[cnt+1] == 'D':
                sumB += CD
                cntC += CD
            elif LB[cnt+1] == 'M':
                sumB += CM
                cntC += CM
            else:
                sumB += C
        else:
            sumB += C
    elif i == 'L':
        sumB += L
    elif i == 'X':
        if cnt < len(LB)-1 and cntX == 0:
            if LB[cnt+1] == 'L':
                sumB += XL
                cntX += XL
            elif LB[cnt+1] == 'C':
                sumB += XC
                cntX += XC
            else:
                sumB += X
        else:
            sumB += X
    elif i == 'V':
        sumB += V
    elif i == 'I':
        if cnt < len(LB)-1 and cntI == 0:
            if LB[cnt+1] == 'V':
                sumB += IV
                cntI += IV
            elif LB[cnt+1] == 'X':
                sumB += IX
                cntI += IX
            else:
                sumB += I
        else:
            sumB += I
    cnt += 1

if cntI == IV:
    sumB -= V
elif cntI == IX:
    sumB -= X
if cntX == XL:
    sumB -= L
elif cntX == XC:
    sumB -= C
if cntC == CD:
    sumB -= D
elif cntC == CM:
    sumB -= M

sumAB = sumA + sumB
print(sumAB)

RAB = ''
while sumAB != 0:
    if sumAB >= 1000:
        RAB += 'M'
        sumAB -= 1000
    elif sumAB >= 900:
        RAB += 'CM'
        sumAB -= 900
    elif sumAB >= 500:
        RAB += 'D'
        sumAB -= 500
    elif sumAB >= 400:
        RAB += 'CD'
        sumAB -= 400
    elif sumAB >= 100:
        RAB += 'C'
        sumAB -= 100
    elif sumAB >= 90:
        RAB += 'XC'
        sumAB -= 90
    elif sumAB >= 50:
        RAB += 'L'
        sumAB -= 50
    elif sumAB >= 40:
        RAB += 'XL'
        sumAB -= 40
    elif sumAB >= 10:
        RAB += 'X'
        sumAB -= 10
    elif sumAB >= 9:
        RAB += 'IX'
        sumAB -= 9
    elif sumAB >= 5:
        RAB += 'V'
        sumAB -= 5
    elif sumAB >= 4:
        RAB += 'IV'
        sumAB -=4
    elif sumAB >= 1:
        RAB += 'I'
        sumAB -= 1

print(RAB)
