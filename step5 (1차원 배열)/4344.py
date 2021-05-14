C = int(input())
for i in range(C):
    student = list(map(int, input().split()))
    countS = 0
    sumS = 0
    AverageS = 0
    for j in range(1, len(student)):
        sumS += student[j]
    AverageS = sumS/student[0]
    for k in range(1, len(student)):
        if(student[k] > AverageS):
            countS += 1
    countAS = round(countS/student[0]*100, 3)
    print("%.3f%%" % countAS)
    
