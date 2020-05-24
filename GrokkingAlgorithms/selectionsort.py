def selectionsort(s):
    if len(s) < 2:
        return s
    else:
        l = len(s)
        for i in range(0,l):
            minindex = i
            for j in range(i+1,l):
                if s[j] < s[minindex]:
                    minindex = j
            if minindex != i:
                s[i], s[minindex] = s[minindex], s[i]
        return s

print(selectionsort([12,3,45,36,27,63,28,85,99,100,3,7,11,81,18,28,83,39,94]))

