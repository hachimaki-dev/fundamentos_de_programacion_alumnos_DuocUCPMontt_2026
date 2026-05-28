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
        print("Vuelo registrado con {pasajeros} pasajeros.")
        print(f"Número recibido: {valor}")
        break
    except ValueError:
        print("Error: ingresa un número entero positivo de pasajeros.")
continuar()