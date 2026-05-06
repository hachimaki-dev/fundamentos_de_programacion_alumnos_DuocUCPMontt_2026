mensajes = ['hola', 'noob', 'genial', 'manco']
palabras_prohibidas = ['noob', 'manco']

for palabra in mensajes:
    if palabra in palabras_prohibidas:
        print('[CENSURADO]')
    else:
        print(palabra)
