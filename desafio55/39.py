respuestas = ["Juan", None, "Ana", ""]
lista_nueva = []
for i in respuestas:
    if i is not None:
        limpio = i.strip()
        if limpio != "":
            lista_nueva.append(limpio)

print(lista_nueva)