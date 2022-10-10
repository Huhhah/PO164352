lista = [1,-2,8,-5,0,5,3]


def ile_ujemnych():
    i = 0
    for x in lista:
        if x<0:
            i = i+1
    return i
print(ile_ujemnych())