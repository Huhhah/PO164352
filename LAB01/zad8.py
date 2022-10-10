list=[]
for i in range(2,1001):
    list.append(i)
for i in range(2,101):
    for x in list:
        if((x!=i)and(x%i==0)):
            list.remove(x)

print(list)