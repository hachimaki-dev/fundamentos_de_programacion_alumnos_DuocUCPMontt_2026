"""Ejercicio 23: Bloqueo de Seguridad (Cajero)
Haz que el cajero se bloquee si alguien intenta adivinar tu clave muchas veces.

Datos Iniciales: Tienes un contador de intentos fallidos que parte en 0.

Reglas de Negocio: Imagina que el sistema está siempre prendido esperando una clave (un ciclo infinito). 

Si alguien pone mal la clave, sumas 1 al contador. Cuando el contador llegue a 3, el sistema debe imprimir 'Bloqueo de Tarjeta' y apagarse de inmediato para evitar un robo.

Restricciones: Inicia tu ciclo con `while True:`. La única forma de apagar el programa es poner un `if` adentro que use la palabra mágica `break`."""
import time

Intentos_Fallidos = 0

Clave_Numerica = 1234

while Intentos_Fallidos != 3:
    time.sleep(0.5)
    Contraseña = int(input("Introduce tu Clave numerica "))
    if Contraseña == Clave_Numerica:
        time.sleep(0.5)
        print("Clave correcta")
        break
    else:
        time.sleep(0.5)
        print("Clave incorrecta")
        Intentos_Fallidos += 1
        Intentos_Restantes = 3 - Intentos_Fallidos
        time.sleep(0.5)
        print(f"Intentos restantes: {Intentos_Restantes}")
        
if Intentos_Fallidos == 3:
    time.sleep(0.5)
    print("Tarjeta bloqueada por seguridad")