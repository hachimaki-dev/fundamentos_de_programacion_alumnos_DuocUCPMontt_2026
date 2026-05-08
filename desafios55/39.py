respuestas = ["juan", None, "", "Ana", " "]
lista_limpia = []
for respuesta in respuestas:
    if respuesta is not None:
        respuesta_limpia = respuesta.strip()
        if respuesta_limpia != "":
            lista_limpia.append(respuesta_limpia)
print(lista_limpia)
