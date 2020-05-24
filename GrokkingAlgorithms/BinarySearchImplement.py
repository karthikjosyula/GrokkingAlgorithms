def bst(list1, key):
    list1.sort()
    print(list1)
    low = 0
    high = len(list1) -1
    Found = False
    mid  = 0
    while low <= high and not Found:
        mid  = (low + high) //2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if Found == True:
        print("found the key at position : {}".format(mid))
    else:
        print("Key not found in the list")

key = int(input("enter the search number: "))
bst([23,5,6,1,7,8,4], key)
