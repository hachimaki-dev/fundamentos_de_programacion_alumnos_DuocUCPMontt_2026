respuestas = ['Juan', None, '', 'Ana', ' ']

respuestas_validas = []


for r in respuestas:

    if r is not None and r.strip() != '':
        respuestas_validas.append(r)


print(respuestas_validas)

