contador = 0
curso_nombres = ['Julian', 'Hernan', 'Diego', 'Gonzalo', 'Zobeiba']
curso_edad = ['???', '???', '???', '???', '???']
# opcion = int(input("¿Que datos quiere extraer? "))
# print(f"Datos recibidos: \n{curso_nombres[opcion]} \n{curso_edad[opcion]}")

for nombre, edad in zip(curso_nombres, curso_edad):
    contador += 1
    print(f"El nombre es: {nombre} \nSu edad es: {edad} \nEste dato es el N°{contador}\n")