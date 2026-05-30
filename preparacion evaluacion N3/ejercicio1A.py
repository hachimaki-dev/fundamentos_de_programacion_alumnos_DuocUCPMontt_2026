while True:
    try:
        int(input("ingrese un numero: "))
        break
    
    except ValueError:
        print("porfavor ingrese un numero entero ")
        