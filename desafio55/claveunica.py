#Simula el ingreso a tu cuenta con una clave secreta.

#Datos Iniciales: Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave 'Admin123'.

#Reglas de Negocio: La clave correcta es 'secreto'. Si la clave que escribiste es igual a la correcta, entraste. Si es diferente, suma 1 a tus intentos fallidos.

#Restricciones: Usa un bloque `if/else`. Como en este caso la clave está mal, imprime exactamente: `'Intentos fallidos: '` seguido del número de intentos.
contador = 0
clave_correcta = "secreto"
clave = input("Ingrese clave")
if clave == clave_correcta:
    print("entraste!")
else:
    contador = contador + 1
    print(f"intentos fallidos :{contador}")