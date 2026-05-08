respuestas = ["Juan", None, '', "Ana", ' ']
limpia = []

for vacio in respuestas:
    if vacio is not None and vacio.strip() != '':
        limpia.append(vacio)

print(limpia)