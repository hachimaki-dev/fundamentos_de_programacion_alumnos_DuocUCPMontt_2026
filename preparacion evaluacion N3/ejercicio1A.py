while True:
    try:
        valor = int(input("ingrese un numero: "))
        print(f"numero recibido: {valor}")
        break
    
    except ValueError:
        print("porfavor ingrese un numero entero ")
        