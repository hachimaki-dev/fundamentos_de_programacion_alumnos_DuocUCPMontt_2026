lista_insultos = ['hola', 'noob', 'genial', 'manco']

for i in range(len(lista_insultos)):
    if lista_insultos[i] in ["noob", "manco"]:
        lista_insultos[i] = "[CENSURADO]"
print(lista_insultos)