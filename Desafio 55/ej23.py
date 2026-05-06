#Ejercicio 23: Bloqueo de Seguridad (Cajero)
#Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.

#Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.

#Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.

#Restricciones: Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`.

intentos_fallidos = 0
intentos_maximos = 3

clave = "12345"

while True:
    password = int(input("Ingresa tu clave: "))

    if password == clave:
        print("Bienvendo a Banco Estado")
        break
    else:
        intentos_fallidos += 1
        print(f"\nFallaste\nGastate {intentos_fallidos} intento/s")

        if intentos_fallidos >= intentos_maximos:
            print("\n=======Bloqueo Tarjeta=======")
            break