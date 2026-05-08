#Tienes un contador de intentos fallidos que parte en 0.

intentos_fallidos = 0
clave_buena = "1234"

while True: 
    clave = input("Ingresa clave: ")


    if clave == clave_buena:
        print("Acceso Concedido")
        break
    else:
        if intentos_fallidos == 3:
            print("TARJETA BLOQUEADA")
            break
