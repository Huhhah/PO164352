list=[31,28,31,30,31,30,31,31,30,31,30,31]

def minmax():
    list2=[]
    list2.append(min(list))
    list2.append(max(list))
    return tuple(list2)


print(minmax())
