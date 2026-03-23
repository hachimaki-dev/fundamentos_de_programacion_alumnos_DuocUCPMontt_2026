print("==========================================")
print("====Bienveido a la calculador de python===")
print("==========================================")

print("Seleccione la operación que desea realizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Dividir")

Opcion = int (input("Ingrese el número de la operación que desea utilizar : "))
Numero_1 = int(input ("Ingrese su primer número : "))
Numero_2 = int(input ("Ingrese su segundo número : "))

if Opcion == 1: 
    resultado = Numero_1 + Numero_2
    print ("El resultado de la suma es :" + str(resultado))

elif Opcion == 2:
    resultado = Numero_1 - Numero_2
    print ("El resultado de la resta es : " + str (resultado))

elif Opcion == 3:
    resultado = Numero_1 * Numero_2
    print ("El resultado de la multipliucación es : " + str (resultado))

elif Opcion == 4:
    if Numero_1 or Numero_2 != 0:
     resultado = Numero_1 / Numero_2
     print ("El resultado de la division es : " + str (resultado))
    
    else:
        print ("Error: no se puede dividir por 0")

else :
    print ("Por favor seleccione una operación 1 al 4.")



