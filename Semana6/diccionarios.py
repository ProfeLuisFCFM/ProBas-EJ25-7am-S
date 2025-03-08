dic1 = {}

dic2 = dict()

dic3 = {'Paralelepípedo': 'Es un cuerpo geométrico formado por seis caras, cuya característica principal es que todas sus caras son paralelogramos y además sus caras opuestas son paralelas entre sí.'}

print(dic3['Paralelepípedo'])

dic4 = {'AreaTríangulo': lambda b,h: b*h/2}

print(dic4['AreaTríangulo'](7,4))

print(dic4.keys())

print(dic4.values())


dic5={'a':4,'e':5}

print(dic5)

dic5['i'] = 7

dic5['a'] = 7
print(dic5)