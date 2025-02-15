#import math 

#from math import pi 

from math import pi as PI 

from random import randint

print(randint(0,1))

def operacionCirculo(radio=1):
    area = PI * radio**2 
    circunferencia = PI * 2 * radio
    return area, circunferencia


varia, ble = operacionCirculo()
#print(varia, ble)

#print("%s %.10f" % ("hola", operacionCirculo(5)))


def imprimirMenu(bMenuPrincipal):
    bMP = bMenuPrincipal
    menu = """
            ############ MENU ############
            ##                          ##
            ##        1. Salir          ##
            ##                          ##
            ##############################
            """
    while bMP:
        print(menu)
        op = int(input("Ingrese su opción: "))
        if op == 1:
            bMP = False
            break
        else:
            print("Opción Invalida")



imprimirMenu(False)


def argumentosinfinitos(*args):
    lista = list(args)
    lista.sort(reverse=False)
    for ele in lista:
        print(ele)

#argumentosinfinitos(9.0,3.0,5,7,1)    


distanciaR2 = lambda p1,p2: ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

print(distanciaR2([0,0],[1,1]))

peso = lambda m,g=9.81: m*g

print(peso(80,9.81*100))

#Funciones globales

def cocacola(ml):
    return ml * 12


#Funcions de clase / Locales
class oper():
    def suma(self, *num):
        return sum(num) 


Operaciones = oper()

print(Operaciones.suma(1,2,3,4,5,6,7,8,9,10))


#Funciones en linea / Funciones Lambda

imc = lambda h,w: w/h**2

def cualitativo(imc):    
    if imc >= 0 and imc <= 18.49:
        print("Peso Bajo")
    elif imc >= 18.5 and imc <=24.99:
        print("Peso Normal")
    elif imc >= 25 and imc <=29.99:
        print("Sobre Peso")
    elif imc >= 30 and imc <=34.9:
        print("Obesidad leve")
    elif imc >= 35 and imc <=39.99:
        print("Obesidad media")
    elif imc >= 40:
        print("Obesidad mórbida")
    else:
        print("Datos incorrectos")
    

bAsk = True
h1 = 0.0
w1 = 0.0
while bAsk:
    h1 = float(input("Ingeresa tus altura en m: "))
    w1 = float(input("Ingeresa tus peso en Kg: "))
    cualitativo(imc(h1,w1))
    op = input("Desea continuar? (S/N): ")
    if op.upper() == 'N':
        bAsk = False
        break
        

    

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(h=10, w=0, txt="hello world", border=1)
pdf.output("hello_world.pdf")