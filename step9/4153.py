while(True):
    x, y, z = map(int, input().split())
    if x==0 and y==0 and z==0:
        break
    Max = max(x, y, z)
    Min = min(x, y, z)
    Mid = (x+y+z) - Max - Min
    if Max**2 == (Mid**2 + Min**2):
        print("right")
    else:
        print("wrong")
