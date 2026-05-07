formularios = ["Juan", None, "", "Ana", ""]
lista_limpia = []
for element in formularios:
    if element is not None:
        nombre_limpio = element.strip()
        if nombre_limpio != "":
            lista_limpia.append(element)
print(lista_limpia)