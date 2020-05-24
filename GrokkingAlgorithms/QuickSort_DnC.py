def quicksortDnC(s):
    if len(s) < 2:
        return s  #array with 0, 1 elements is already sorted
    else:
        pivot = s[0]
        lessarray = [i for i in s[1:] if i<=pivot]
        greaterarray = [i for i in s[1:] if i > pivot]
        return quicksortDnC(lessarray)+[pivot]+quicksortDnC(greaterarray)
print(quicksortDnC([100,23,4,78,65,12,34,54,10,1,45,89,651]))
