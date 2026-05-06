"""Ejercicio 11: Clave Única Básico
Simula el ingreso a tu cuenta con una clave secreta.

Datos Iniciales: Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave 'Admin123'.

Reglas de Negocio: La clave correcta es 'secreto'. Si la clave que escribiste es igual a la correcta, entraste. Si es diferente, suma 1 a tus intentos fallidos.

Restricciones: Usa un bloque `if/else`. Como en este caso la clave está mal, imprime exactamente: `'Intentos fallidos: '` seguido del número de intentos."""

Intento_Fallidos = 0

Respuesta = "Admin123"

Clave_secreta = "Secreto"

if Clave_secreta == Respuesta:
    print("Contraseña correcta")
if Clave_secreta != Respuesta:
    Intento_Fallidos += 1
    print(f"Intentos fallidos: {Intento_Fallidos}")
    Respuesta = input("Contraseña ")
    if Clave_secreta == Respuesta:
        print("Contraseña correcta")
    if Clave_secreta != Respuesta:
        Intento_Fallidos += 1
        print(f"Intentos fallidos: {Intento_Fallidos}")
        Respuesta = input("Contraseña ")
        if Clave_secreta == Respuesta:
            print("Contraseña correcta")
        if Clave_secreta != Respuesta:
            Intento_Fallidos += 1
            print(f"Intentos fallidos: {Intento_Fallidos}")
            Respuesta = input("Contraseña ")
            if Clave_secreta == Respuesta:
                print("Contraseña correcta")
            if Clave_secreta != Respuesta:
                Intento_Fallidos += 1
                print(f"Intentos fallidos: {Intento_Fallidos}")
                Respuesta = input("Contraseña ")