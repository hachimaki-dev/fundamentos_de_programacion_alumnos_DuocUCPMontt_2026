mensajes = ['hola', 'noob', 'genial', 'manco']

for palabra in mensajes:
    if palabra == 'noob' or palabra == 'manco':
        print('[CENSURADO]')
    else:
        print(palabra)