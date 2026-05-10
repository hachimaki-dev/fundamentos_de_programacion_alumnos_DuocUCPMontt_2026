respuestas = ["Juan", None, "", "Ana", " "]

limpios = []

for elem in respuestas:
    if elem is not None and elem.strip() != "":
        limpios.append(elem.strip())

print(limpios)