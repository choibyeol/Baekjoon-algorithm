H, M = map(int, input().split())

if(M >= 45):
    print("%d %d" % (H, M - 45))
else:
    if(H == 0):
        print("%d %d" % (24-1, 60-(45-M)))
    else:
        print("%d %d" % (H-1, 60-(45-M)))
