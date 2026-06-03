def continuar():
    while True:
        respuesta = input("¿Deseas continuar? (Responder con ´SI´ o ´NO´)").upper()
        if respuesta == "SI":
            print("Perfecto, continuamos")
            break
        elif respuesta == "NO":
            print("Vale. Cerrando programa")
            import sys
            sys.exit()
        else:
            print("Ingrese una respuesta válida")

while True:
    try:
        valor = int(input("Ingrese un número"))
        print(f"Número recibido: {valor}")
        break
    except ValueError:
        print("Caracter inválido.  ValueError")
continuar()
while True:
    try:
        pasajeros = int(input("Ingrese la cantidad de pasajeros para el vuelo"))
        print(f"Vuelo registrado con {pasajeros} pasajeros.")
        break
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")
continuar()
while True:
    try:
        cantidad = int(input("Ingrese el stock de la farmacia"))
        print(f"Stock registrado: {cantidad} unidades disponibles.")
        break
    except ValueError:
        print("Dato inválido. Ingresa un entero positivo para el stock.")
continuar()
    try:
        edad = int(input("¿Qué edad tiene?"))
        print(f"La edad registrada es: {edad} años")
        break
    except ValueError:
        print("Dato inválido")
continuar()
print("A continuación vas a ingresar tu nombre. Solamente pueden ser 6 caracteres y sin espacios")
while True:
    nombre = input("Ingrese su nombre")
    if len(nombre) >= 6 and " " not in nombre:
        print("Nombre ingresado con éxito")
        break
    else:
        print("Nombre invalido")
continuar()
print("A continuación vas a ingresar el codigo de nu producto. Solamente pueden ser 6 caracteres y sin espacios")
while True:
    codigo = input("Ingresar el codigo")
    if len(codigo) >= and " " not in codigo:
            print("Codigo ingresado con éxito")
            break
    else:
        print("Codigo invalido")
continuar()
print("Ingrese el codigo de su patente, recuerde que su patente SOLO puede tener 6 caracteres y sin espacios")
while True:
    patente = input("Ingrese su patente")
    if len(patente) == 6 and " " not in patente:
        print("Patente ingresada con exito")
        break
    else:
        print("Codigo de patente invalido")
continuar()
contador_baja = 0
contador_media = 0
contador_alta = 0
print("Bienvenido a la clasificación de temperaturas en una planta industrial")
while True:
    print("Ingrese la temperatura que desea ingresar (Ingresar 00 para salir)")
    temperatura = float(input("Ingrese su temperatura"))
    if temperatura == 00:
        print("Perfecto, saliendo")
        break
    else:
        if temperatura < 50:
            print("Temperatura Baja")
            contador_baja += 1
        elif temperatura >= 50 and temperatura <= 80:
            print("Normal operativo")
            contador_media += 1
        else:
            print("ALERTA. TEMPERATURA CRITICA")
            contador_alta += 1
print("Lectura de estado")
print(f"Temperatura baja: {contador_baja}")
print(f"Temperatura Normal: {contador_media}")
print(f"Temperatura CRITICA: {contador_alta}")
continuar()
