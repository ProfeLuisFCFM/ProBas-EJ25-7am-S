lista1 = []
lista2 = list()

lista1.append(1)

print(lista1)
lista1.clear()
print(lista1)

lista1 = [1,2,3]
lista2 = lista1.copy()

print(lista1,lista2)

lista1.append(4)

print(lista1,lista2)

print(lista2.count(1)+lista2.count(2))

lista1.extend(lista2)

print(lista1)

lista100 = [n for n in range(1,101)]

print(lista100)

lista100.insert(31,33)

print(len(lista100))

