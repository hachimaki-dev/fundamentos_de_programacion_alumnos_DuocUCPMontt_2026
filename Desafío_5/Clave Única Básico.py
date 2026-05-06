Intentos_Fallidos = 0
Contraseña = "abc"


while Intentos_Fallidos < 3 : 

    Usuario = str(input ("Ingrese su clave : ")).lower()

    if Usuario == "abc":
        print ("Has accecido.")
        print (f"tus intentos han sido {Intentos_Fallidos}")
        break

    else :
        print ("Contrseña incorrecta.")
        Intentos_Fallidos += 1
        print (f"\nLLevas un total de {Intentos_Fallidos} fallos")