#Ejercicio 23: Bloqueo de Seguridad (Cajero)
#Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.

#Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.

#Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito).
#Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir
#'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.

#Restricciones: Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`.

contador_fallos=0
clave_real="1234"
intentos=3

while True:
    clave_usu=input("\nIngrese Clave ")

    if clave_usu==clave_real:
        print("Acceso concedido\n")
        break

    intentos=intentos-1
    print("\nCLAVE INVALIDA")

    if intentos>0:
        if intentos==1:
            print(f"Tines {intentos} intento, de lo contrario se bloqueara")
        else:
            print(f"Tines {intentos} intentos, de lo contrario se bloqueara")
    else:
        print("Bloqueo de Tarjeta\n")
        break
    
        