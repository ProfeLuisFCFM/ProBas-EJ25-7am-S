#normalita -> función global
#con definición -> función en clase (local)
#Lambda -> función Lambda


def Discriminante(a,b,c,z=0):
    return b**2 - 4*a*c

def FormulaGeneral(a,b,c):
    d = Discriminante(a,b,c)
    if d > 0:
        x1 = (-b + d**0.5)/2*a
        x2 = (-b - d**0.5)/2*a
    elif d == 0:
        x1 = x2 = -b/2*a
    else:
        x1 = (-b + ((-1*d)**0.5*complex('0+1j')))/2*a
        x2 = (-b - ((-1*d)**0.5*complex('0+1j')))/2*a
    return x1,x2


#print(FormulaGeneral(1,2,1),"caso d=0")
#print(FormulaGeneral(1,4,1),"caso d>0")
#print(FormulaGeneral(1,1,1),"caso d<0")


#### Función Local (de clase)


class Vehiculos(): #Declaración de clases
    def __init__(self,VelMax):
        self.VelMax = VelMax
    
    def printVelMax(self):
        print("La velocidad Máxima es:", self.VelMax)

class Aereos(Vehiculos): #Clase con Herencia
    def __init__(self,VelMax,AltMax):
        self.AltMax = AltMax
        super().__init__(VelMax)

    def printAltMax(self):
        print("La altitud máxima es:",self.AltMax)
        



#Helicopter = Aereos(100,400)
#Helicopter.printVelMax()
#Helicopter.printAltMax()




#print(type(Helicopter))


#### Funciones Lambda --> Functioninline

#nombre = lambda args: loquevareturn

#peso = lambda masa,gravedad=9.81: masa*gravedad

#print(peso(130,24.79))


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n




'''
factorial(5) -> 5*factorial(4)
factorial(4) -> 4*factorial(3)
factorial(3) -> 3*factorial(2)
factorial(2) -> 2*factorial(1)
factorial(1) -> 1*factorial(0)
factorial(0) -> 1

factorial(1) -> 1*1
factorial(2) -> 2*1
factorial(3) -> 3*2
factorial(4) -> 6*4
factorial(5) -> 24*5 -> 120




'''

#Scope -> Alcance


from problema2 import espera


def promedioListaEstrella(*Args):
    print(list(Args))

print(promedioListaEstrella(12,2,3,4,5,6,76))


if __name__ == '__main__':
    print(factorial(5))


