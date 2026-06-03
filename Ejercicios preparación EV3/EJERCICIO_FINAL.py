bandera = True
while bandera:
    while bandera:
        try:
            animales_registrados = int(input("¿Cuantos animales va a ingresar a la veterinaria?"))
            break
        except:
            ValueError()
            print("Por favor, ingrese caracter válido")

    if animales_registrados >= 1:
        print(f"Se ha regitrado con éxito la siguiente cantidad: {animales_registrados}")
        while bandera:
            pregunta = input("¿Estas seguro de la cantidad seleccionada? (responder con 'SI' o 'NO'))").upper()
            if pregunta == "SI":
                print("Perfecto, entonces continuamos")
                bandera = False
            elif pregunta == "NO":
                print("Perfecto, entonces volvemos")
                break
            else:
                print("Ingresar caracter valido")
    else:
        print("Ingresar un número mayor o igual a 1")
print("Ahora, le vamos a preguntar el nombre y peso de cada uno de sus animales")
print("El nombre tiene que tener al menos 6 caracteres y SIN espacios")
print("El peso tiene que ser un entero positivo")

bandera1 = True
while bandera1:
    bandera_recordatorio = True
    nombres_animales = []
    bandera2 = True
    bandera3 = True
    contador = animales_registrados
    contador = 1
    while bandera2:
        if bandera_recordatorio == False:
            print("Pequeño recordatorio")
            print("El nombre tiene que tener al menos 6 caracteres y SIN espacios")
        while bandera3:
            nombre_animal = input(f"Ingrese el nombre de su animal {contador}")
            if len(nombre_animal) >= 6 and " " not in nombre_animal:
                    pregunta = input(f"¿Estas seguro de que el nombre es {nombre_animal}? (responder con 'SI' o 'NO'))").upper()
                    if pregunta == "SI":
                        print("Perfecto, entonces continuamos")
                        nombres_animales.append(nombre_animal)
                        contador += 1
                        bandera_recordatorio = False
                        break
                    elif pregunta == "NO":
                        print("Perfecto, entonces volvemos")
                    else:
                        print("Ingresar caracter valido")
            else:
                print("Nombre inválido")
        if contador == animales_registrados + 1:
            print(nombres_animales)
            pregunta = input(f"¿Estas bien con tus respuestas, o quieres volver a empezar con la misma cantidad seleccionada ({animales_registrados} animales) (responder con 'SI' para continuar.'NO' para reiniciar)?").upper()
            if pregunta == "SI":
                print("Perfecto, continuamos")
                bandera1 = False
                bandera2 = False
                bandera3 = False
            elif pregunta == "NO":
                print("Perfecto, entonces vamos de nuevo")
                bandera2 = False
                bandera3 = False

bandera1 = True
while bandera1:
    bandera_recordatorio = True
    peso_animales = []
    bandera2 = True
    bandera3 = True
    contador = animales_registrados
    contador = 1
    while bandera2:
        if bandera_recordatorio == False:
            print("Pequeño recordatorio")
            print("El peso tiene que ser un número positivo igual o mayor a 1")
        while bandera3:
            for animal in nombres_animales:
                while bandera3:
                    while True:
                        try:
                            peso_animal = int(input(f"Ingrese el peso de {animal}"))
                            break
                        except:
                            ValueError()
                            print("Ingrese un caracter válido")
                    if peso_animal >= 1:
                            pregunta = input(f"¿Estas seguro de que el peso de {animal} es {peso_animal} Kg? (responder con 'SI' o 'NO'))").upper()
                            if pregunta == "SI":
                                print("Perfecto, entonces continuamos")
                                peso_animales.append(peso_animal)
                                bandera_recordatorio = False
                                break
                            elif pregunta == "NO":
                                print("Perfecto, entonces volvemos")
                            else:
                                print("Ingresar caracter valido")
            print(peso_animales)
            pregunta = input(f"¿Estas bien con tus respuestas, o quieres volver a empezar? (responder con 'SI' para continuar.'NO' para reiniciar)?").upper()
            if pregunta == "SI":
                print("Perfecto, continuamos")
                bandera1 = False
                bandera2 = False
                bandera3 = False
            elif pregunta == "NO":
                print("Perfecto, entonces vamos de nuevo")
                bandera2 = False
                bandera3 = False


peso_grande = []
contador_grande = 0
peso_pequeño = []
contador_pequeño = 0

for peso in peso_animales:
    if peso > 25:
        peso_grande.append(peso)
        contador_grande += 1
    else:
        peso_pequeño.append(peso)
        contador_pequeño += 1



print(f"De los siguientes animales {nombres_animales}, hay {contador_grande} catalogado/s como PESO GRANDE y {contador_pequeño} catalogado/s como PESO PEQUEÑO")
print(f"PESO GRANDE = {peso_grande}")
print(f"PESO PEQUEÑO = {peso_pequeño}")