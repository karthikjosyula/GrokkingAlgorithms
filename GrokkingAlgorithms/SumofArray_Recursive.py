def sumarray_recursive(s):
    if len(s)==0:
        return 0
    else:
        i = s[0]
        s.pop(0)
        return i + sumarray_recursive(s)

print(sumarray_recursive([1,5,6,8,22,23,456,76]))
