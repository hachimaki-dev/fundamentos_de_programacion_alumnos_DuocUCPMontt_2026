#Ejercicio : Ejercicio 23: Bloqueo de Seguridad (Cajero)
#MEDIUM
#Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.[cite: 2]

#Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.[cite: 2]

#Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.[cite: 2]

#Restricciones: Inicia tu ciclo con while True:. La única forma de apagar el programa es poner un if adentro que use la palabra mágica break.[cite: 2]

intentos_fallidos = 0
clave_secreta = 6767
clave_insertada = 0
while True :
    clave_insertada = int(input("Inserte su clave "))
    if clave_insertada != clave_secreta :
        intentos_fallidos = intentos_fallidos + 1
        print(f"Te has equivocado baboso, intento fallido N°{intentos_fallidos}")
        if intentos_fallidos == 3 :
            print(f"Ya te rifaste, llegaste al número máximo de errores. Tarjeta Bloqueada")
            break
    elif clave_insertada == clave_secreta :
        print("Acceso Permitido")
        break
