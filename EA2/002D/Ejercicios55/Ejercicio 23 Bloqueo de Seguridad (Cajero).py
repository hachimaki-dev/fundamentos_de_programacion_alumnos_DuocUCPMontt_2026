# Ejercicio 23: Bloqueo de Seguridad (Cajero)
# Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.

# Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.

# Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.

# Restricciones: Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`.

intentos_fallidos = 0
pin = 1234

while 3 > intentos_fallidos:
    intento_pin = int(input("Ingrese su pin: "))
    if intento_pin != pin:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Bloqueo de Tarjeta")
            break
    else:
        "Acceso permitido"
