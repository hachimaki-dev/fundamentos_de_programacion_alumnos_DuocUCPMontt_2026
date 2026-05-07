#Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.

#Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.

#Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.

#Restricciones: Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`.


clave_de_acceso = "alexander123"
intentos_fallidos = 0
while True:
    clave_de_acceso = input("ingrese la clave de acceso:")
    if clave_de_acceso != "alexander123":
        intentos_fallidos += 1
    if intentos_fallidos == 3:
        print("bloque de tarjeta")
        break
