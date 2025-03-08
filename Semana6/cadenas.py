#for _ in range(10):
#    print("hola mundo",_)


str() 


modelo = 'Hello Kitty'

#for l in modelo:
#    print(l)
#Iterable

modelo = modelo.capitalize()

print(modelo)

#modelo.encode('utf8')

modelo += ' á'

print(modelo)

if modelo.endswith('á'):
    print("simón")

if modelo.startswith('He'):
    print("abuelita de batman")

print(modelo.find('kitti'))

print('{:.6f}'.format(1))

print(modelo.index('o'))

print(modelo.join('he'))

interchange = {32: 64}

print(modelo.translate(interchange))

modelo = modelo.swapcase()

print(modelo)
modelo.zfill()