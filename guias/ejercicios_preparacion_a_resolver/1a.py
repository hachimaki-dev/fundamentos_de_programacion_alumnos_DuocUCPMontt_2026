

while True:

    try:
       ingresar_numero = int(input("Ingresa un numero: "))
       print(f"Numero recibido {ingresar_numero}")
       break



    


    except ValueError :

        print("Error: eso no es un numero entero: ")