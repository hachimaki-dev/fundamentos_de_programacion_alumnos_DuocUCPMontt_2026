opcion = 0 
print("Calculadora")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
opcion = int(input("Ingrese su opcion :"))
match opcion:
    case 1:
     print("Cargando")
     sys.sleep(5)
     suma =int(input("Ingrese un numero"))
     suma2 = int(input("Ingrese otro numero"))
     resultado = suma + suma2
     print("Cargando su resultado : ")
     sys.sleep(5)
     print(f"El resultado es : {resultado}")

    case 2:
      resta = int(input("Ingrese un numero: "))
      resta2 = int(input("Ingrese otro numero : "))
      resultado = resta - resta2
      print(f"Su resultado es : {resultado}")

    case 3:
     multi1 = int(input("Ingrese un numero:"))
     multi2 = int(input("Ingrese otro numero :"))
     resultado = multi1*multi2
     print("Cargando su resultado..")
     print(f"El resultado es : {resultado}")
    case 4:
     divi1= int(input("Ingrese un numero : "))
     divi2= int(input("Ingrese otro numero"))
     resultado = divi1/divi2
     print(f"Su resultado es : {resultado}")