curso = ['Benja', 20, 'Marron', 'Barbara', 20, 'negro']

curso_nombres = ['Benja', 'Barbara', 'Diego']
curso_edad = [18, 18, 19]
curso_ojos = ['Cafe', 'Cafe', 'Cafe']

print(f"Nombre : {curso_nombres[0]}")
print(f"Edad : {curso_edad[0]}")
print(f"Color de ojos : {curso_ojos[0]}")
print(f"Nombre : {curso_nombres[1]}")
print(f"Edad : {curso_edad[1]}")
print(f"Color de ojos : {curso_ojos[1]}")
print(f"Nombre : {curso_nombres[2]}")
print(f"Edad : {curso_edad[2]}")
print(f"Color de ojos : {curso_ojos[2]}")

print(f"El tamaño de la lista de nombres es {len(curso_nombres)}")

print(f"El ultimo vale {len(curso_nombres)}")

contador = 0
for nombre in curso_nombres :
    print(f"El nombre numero {contador} es {nombre}")
    contador = contador + 1