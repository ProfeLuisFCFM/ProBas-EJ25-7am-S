numA = 7# int(input("ingrese A: "))
numB = 8# int(input("ingrese B: "))

pregunta1 = numA > numB
print(pregunta1,type(pregunta1))
if pregunta1:
    print("A mayor que B")
else:
    print("B mayor que A")


matricula = 0

#codigo que busca matricula

#Retorna en la variable matricula si la encontró

if not bool(matricula):
    print("no se encontró matricula")
else:
    print("matricula: ", matricula)


#Casos donde bool es False

b1 = bool(0)
b2 = bool(0.0000000000)
b3 = bool("")

c1 = bool([])
c2 = bool(())
c3 = bool(set())
c4 = bool({})

cc1 = bool(range(0))
cc2 = bool(enumerate([])) 

print(b1,b2,b3)

print(c1,c2,c3,c4)

print(cc1,cc2)

print(None,type(None))


l1 = [1, 2, 3, 4, 5]

if 6 in l1:
    print("Está")
else:
    print("No está")


print(bool(None))



#Estructura FOR

#iterador = list([1,2,3,4,5]), tuple((n)), range(1,2,0.5), dict(), set()

#for var in iterador:
#    print(var)


saludo = dict()

saludo["Español"] = "Hola mundo"
saludo["Inglés"] = "Hello world"

print(saludo)


keys = saludo.keys()

values = saludo.values()

tupla = saludo.items()

print(keys,values,tupla)
print(type(keys),type(values),type(tupla))


for k, v in saludo.items():
    print(k,v)

from random import randint
ctrl = False
while ctrl:
    print("1. Imprime Hola \n 2. Aleatorio \n 3. Salida")
    op = int(input("Introduzca la opción: "))
    if op == 1:
        print("hola we")
    elif op == 2:
        print(randint(0,100))
    else:
        ctrl = False


mensajes = ['Estás seguro?', 'Seguro, seguro?', 'Super seguro?', 'conste que no hay vuelta a atrás eh!!', "Te lo advertí", "borrando historial de chrome"]

from random import randint
ctrl = False
while ctrl:
    print("1. Imprime Hola \n2. Aleatorio \n3. Salida")
    op = int(input("Introduzca la opción: "))
    if op == 1:
        print("hola we")
    elif op == 2:
        print(randint(0,100))
    elif op == 3:
        for msg in mensajes:
            op2 = input("Ingresa [y] para continuar: ")
            if op2 == 'y' or op2 == 'Y':
                 print(msg)
        ctrl = False         
    else:
        print("opción invalida")


# Listas

lista1 = list()
lista2 = []

#Agregar elementos
lista1.append("loquesea")
lista1.append(None)

#Borrar toda la lista
#lista1.clear()

#Importancia del copy
lista2 = lista1.copy()

lista2.append("querollo?")

lista2.append("querollo?")

lista2.append("querollo?")
#print(lista1,lista2)

#Imprime la cantidad de veces que aparece el elemento buscado

#print(lista2.count("querollo?"))

lista1 = lista1 + lista2

print(lista2)

lista1.extend(lista2)

print(lista1, lista2)

nombre = "Danna Cecilia Carranza Betancourt"

print("La cantidad de palabras son: ",nombre.count(" ")+1)


nombre2 = "Luis Angel Gutierrez Rodriguez"
nombre2 = nombre2.replace(" ", "")

print(len(nombre2))