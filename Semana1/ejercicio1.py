# Descripción: Escribe un programa que solicite al usuario dos números enteros y realice las operaciones aritméticas básicas 
# (suma, resta, multiplicación, división, división de piso y residuo) entre ellos. Muestra los resultados en pantalla.

a = int(input("Ingrese el número a:"))
b = int(input("Ingrese el número b:"))

print("suma: ",a+b)
print("resta: ",a-b, b-a)
print("multiplica: ",a*b, b*a)
print("divide: ",a/b, b/a)
print("divide: ",a//b, b//a)
print("modulo: ",a%b, b%a)
