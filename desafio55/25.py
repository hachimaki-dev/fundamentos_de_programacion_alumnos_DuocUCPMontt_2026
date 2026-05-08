lista = ['hola', 'noob', 'genial', 'manco']

palabras_prohibidas = ['noob', 'manco']

for palabra in lista:
    if palabra in palabras_prohibidas:
        print('[CENSURADO]')
    else:
        print(palabra) 