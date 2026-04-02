normal = 800
estudiante = 250
adulto_mayor = 450

print("Bienvenido al servicio de cobro automatizado")
print("Debera elegir su tipo de tarifa y posteriormente pagar.")

conteo_personas = 0
dinero_ganado = 0
conteo_estudiantes = 0
conteo_adultos_mayores = 0
conteo_normales = 0



while True:
    try:
        respuesta = int(input("Opciones disponibles \n1. Normal\n2. Estudiante\n3. Adulto mayor\n4. CORTE\nDecida su opción: "))
        if respuesta == 1:
            print(f"Elegiste {respuesta}, por lo tanto pagas {normal}")
            dinero_ganado += normal
            conteo_personas += 1
            conteo_normales += 1
        elif respuesta == 2:
            print(f"Elegiste {respuesta}, por lo tanto pagas {estudiante} ")
            dinero_ganado += estudiante
            conteo_personas += 1
            conteo_estudiantes += 1
        elif respuesta == 3:
            print(f"Elegiste {respuesta}, por lo tanto pagas {adulto_mayor}")
            dinero_ganado += adulto_mayor
            conteo_personas += 1
            conteo_adultos_mayores += 1
        elif respuesta == 4:
            break
    except ValueError:
        print("Error, ingresa un número valido.")



    
print("Gracias por usar el servicio.")

print(f"La cantidad total de personas que usaron el servicio fue de: {conteo_personas}")

print(f"La cantidad total de tarifas normales fue de: {conteo_normales}")

print(f"La cantidad total de tarifas estudiantiles fue de: {conteo_estudiantes}")

print(f"La cantidad total de tarifas de tercera edad fue de: {conteo_adultos_mayores}")

print(f"El total del dinero recaudado hoy fue de {dinero_ganado}")