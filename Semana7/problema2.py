def espera():
    frase = input("Ingrese una frase: ")
    #Demo: "Hola Mundo" --> "aloh odnum"
    frase = frase.lower()
    lista = frase.split(' ')
    #frase = "hola mundo" --> ['hola','mundo']
    print(lista)
    for palabra in lista:
        print(palabra[::-1], end=' ')
    print()


    print(type(frase))
    for _ in frase:
        print(_)



    days = ['Luna','Marte','Mercurio','Jupiter','Venus','Saturno','Domingo']

    print(days,"modo normal")

    print(days)
    print(days.reverse(),"usando reverse")
    print(days)

    print(days[::-1], "usando forinline")

    for i in range(len(days)-1,-1,-1): 
        print(days[i])
    print("usando for con comodín")



if __name__ == '__main__':
    espera()