respuestas = ['Juan', None, '', 'Ana', ' ']

respuestas_filtradas = []

for elemento in respuestas:
    if elemento is not None and elemento.strip() != "":
        respuestas_filtradas.append(elemento)

print(respuestas_filtradas)