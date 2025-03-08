class nodo:
    def __init__(self,datos,a=None,s=None):
        self.antecesor = a
        self.datos = datos
        self.sucesor = s

    def __str__(self):
        print(f"{self.antecesor} \n {self.sucesor} \n {self.datos}")

elemento1 = nodo('Luis')
elemento2 = nodo('Jaime')
elemento2.antecesor = elemento1
elemento1.sucesor = elemento2



lista = [elemento1,elemento2]

print(str(lista))
