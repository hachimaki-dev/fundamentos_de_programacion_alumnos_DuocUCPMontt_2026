mensajes_sucios = ['hola', 'noob', 'genial', 'manco']
contador = 0
for i in mensajes_sucios:
    if i == 'noob' or i == 'manco':
        mensajes_sucios[contador] = ['CENSURADO']

    contador += 1

print(mensajes_sucios)