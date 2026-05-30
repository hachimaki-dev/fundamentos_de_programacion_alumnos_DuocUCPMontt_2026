respuestas = ['Juan', None, '', 'Ana', ' ']
respuestas_limpias = []

for respuesta in respuestas:
    if respuesta is not None:
        respuesta_limpia = respuesta.strip()
        if respuesta_limpia != "":
            respuestas_limpias.append(respuesta_limpia)

print(respuestas_limpias)