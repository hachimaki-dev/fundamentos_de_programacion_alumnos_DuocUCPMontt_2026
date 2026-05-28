


while True:
    try:
        numero_entero = int(input("ingrese un numero: "))
        print(f"numero recibido {numero_entero}")
        break
    except ValueError:
        print("eso no es un numero entero")



