contador = 0
curso_nombres = ['Julian', 'Hernan', 'Diego', 'Gonzalo', 'Zobeiba']
curso_edad = ['???', '???', '???', '???', '???']
# opcion = int(input("¿Que datos quiere extraer? "))
# print(f"Datos recibidos: \n{curso_nombres[opcion]} \n{curso_edad[opcion]}")

for nombre in curso_nombres:
    print(f"El nombre es: {nombre}, este dato es el N°{contador}")
    contador += 1