Intento_fallidos = 0

while True :
    clave = int(input("Ingrese su clave : "))
    Intento_fallidos += 1
    print (f"ERROR, clave incorreta, llevas un total de {Intento_fallidos} intentos fallidos")

    if Intento_fallidos > 3:
        print ("BLOQUEO DE TARJETA, APAGANDO PROGRAMA.")
        break

    
        