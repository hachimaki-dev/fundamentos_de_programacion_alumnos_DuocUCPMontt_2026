respuestas = ["Juan", None, "Ana"]
respuestas_correctas = []

for elem in respuestas:
    if elem is not None and elem.strip() != '':
        respuestas_correctas.append(elem)

print(respuestas_correctas)