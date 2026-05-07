# Ejercicio 39: Limpieza de Formulario (Data Science)

print("==========================================")
print("Iniciando limpieza de datos del formulario")
print("==========================================")

respuestas = ['Juan', None, '', 'Ana', ' ']

limpios = []

for elem in respuestas:
    if elem is not None and elem.strip() != '':
        limpios.append(elem)

print(limpios)