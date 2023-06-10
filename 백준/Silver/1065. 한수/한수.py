def numd(a):
    if a < 100:
        return bool(True)
    else:
        numL = list(str(a))
        difS = set([])
        for i in range(1, len(numL)):
            dif = int(numL[i]) - int(numL[i-1])
            difS.add(dif)
        if len(difS) == 1:
            return bool(True)
        else:
            return bool(False)

n = int(input())
c = 0
for i in range (1, n+1):
    if numd(i) == True:
        c += 1
print(c)