#Simula el ingreso a tu cuenta con una clave secreta.
#Datos Iniciales: Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave 'Admin123'.
#Reglas de Negocio: La clave correcta es 'secreto'. Si la clave que escribiste es igual a la correcta, entraste. Si es diferente, suma 1 a tus intentos fallidos.
#Restricciones: Usa un bloque `if/else`. Como en este caso la clave está mal, imprime exactamente: `'Intentos fallidos: '` seguido del número de intentos

intentos_fallidos =0
clave = "secreto"

if input("ingrese su clave: ") == clave:
    clave_correcta = False
else:
    intentos_fallidos += 1
    print(f"intentos fallidos: {intentos_fallidos}")

