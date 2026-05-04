edad = 0

while True:
    try:
     
     edad = int(input("Ingrese su edad para poder continuar \n:"))

     if edad > 17:
      print("usted es mayor de edad, puede continuar")
      break
     else:
       print("usted no cumple con la edad requerida")

    except ValueError:
      print("Ingrese un numero valido")