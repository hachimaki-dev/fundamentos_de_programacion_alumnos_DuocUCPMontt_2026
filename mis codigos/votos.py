print("Ingrese la edad solicitada para póder ingresar")
      
edad = 0

while True:
    try:

     edad = int(input("ingrese su edad \n: "))

     if edad > 17:
        print("puede acceder")
        break
     else:
        print("edad ingresada es menor")

    except ValueError:
        print("edad ingresada es invalida")
    