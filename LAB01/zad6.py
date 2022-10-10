list=[1,4,16,9,9,7,4,9,11]

def suma_przemienna():
    suma=0
    i=0
    for x in list:
        if(i%2==0):
            suma+=x
        else:
            x=x*(-1)
            suma+=x
        i+=1
    return suma

print(suma_przemienna())