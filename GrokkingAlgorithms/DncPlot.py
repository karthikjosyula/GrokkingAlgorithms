def dncplotland(l,b):
    s1 = l
    s2 = b
    if(s1%s2 ==0):
        return s2
    else:
        return dncplotland(s2,s1%s2)

print(dncplotland(1680,640))

