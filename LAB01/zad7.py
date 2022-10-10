lista=[]
while len(lista)<10:
    a=(int(input("Podaj element listy:")))
    if (a in lista):
        continue
    else:
        lista.append(a)
print(lista)