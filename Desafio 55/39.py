respuestas = ['Juan', None, '', 'Ana', ' ']
respuestas_correctas = []

for respuesta in respuestas :
    if respuesta is not None and respuesta.strip() != "":
        respuestas_correctas.append(respuesta)

print(respuestas_correctas)