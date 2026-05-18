respuestas = ["Juan", None, "", "Ana", " "]
lista_nueva = []
for nombre in respuestas:
    if nombre is not None and nombre.strip() != "":
        lista_nueva.append(nombre.strip())

print(lista_nueva)
