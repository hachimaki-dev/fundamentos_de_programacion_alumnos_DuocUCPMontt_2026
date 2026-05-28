
while True:
    try:
    
        respuesta = int(input("ingrese un numero"))
        print(f"Número recibido: {respuesta}")
        break
    except ValueError:
        print("Error: eso no es un número entero.")
