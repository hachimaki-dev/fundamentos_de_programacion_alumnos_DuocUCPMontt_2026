#Ejercicio 39: Limpieza de Formulario (Data Science)
#Limpia los datos sucios que dejó la gente al llenar mal un formulario.

#Datos Iniciales: Recibiste estas respuestas: `['Juan', None, '', 'Ana', ' ']`.

#Reglas de Negocio: Solo sirven los nombres reales. Los espacios en blanco (' '), las respuestas vacías ('') o los datos nulos (`None`) se consideran basura y hay que botarlos. Solo guarda los nombres válidos en una lista nueva.

#Restricciones: Recorre las respuestas. Usa `is not None` para asegurarte de que no sea nulo. Luego usa `.strip()` para borrarle los espacios extra y asegúrate de que no quede vacío `!= ''`. Si pasa las pruebas, guárdalo. Imprime la lista limpia.

#Pista de Ayuda:
#Usa if elem is not None and elem.strip() != '':

answer = ['Juan', None, '', 'Ana', ' ']
lista_limpia = []

for elem in answer:
    if elem is not None and elem.strip() != '':
        lista_limpia.append(elem.strip())

print(lista_limpia)
