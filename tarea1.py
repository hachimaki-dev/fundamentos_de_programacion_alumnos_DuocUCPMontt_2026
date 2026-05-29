while True:
    try:
        num = int(input("Ingresa un número: "))
    
        break
    except ValueError:
        print("Ha ocurrido un error, esperaba un número entero")

print(f"Número recibido: {num}")

