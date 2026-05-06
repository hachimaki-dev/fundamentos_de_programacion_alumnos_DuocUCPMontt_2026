#Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.

#Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.

#Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.

#Restricciones: Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`.
intento_fallido = 0
clave = 3245
while True:
    clave_igresada = int(input("ingrese clave: "))
    if clave_igresada != clave:
        intento_fallido += 1
        if intento_fallido == 3:
            print("tarjeta bloqueada")
            break
    elif clave_igresada == clave:
        print("acceso concedido")
        break