respuestas = ["Juan",None,"","Ana",""]
respuestas_validas = []
for i in respuestas:
    if i is not None and i.strip() != "":
        respuestas_validas.append(i)
print(respuestas_validas)

