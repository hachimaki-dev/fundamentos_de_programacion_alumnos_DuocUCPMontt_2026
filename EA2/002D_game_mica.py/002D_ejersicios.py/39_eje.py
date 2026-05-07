respuestas = ['Juan', None, '', 'Ana', ' ']

for elementos in respuestas:
    if elementos is not None and elementos.strip() != '':
        print(elementos)
