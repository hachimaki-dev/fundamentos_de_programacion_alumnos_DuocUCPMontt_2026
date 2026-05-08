"""
🟡 Rango: Cuidado
Ejercicio 11: Clave Única Básico
Simula el ingreso a tu cuenta con una clave secreta.

Datos Iniciales: Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave 'Admin123'.

Reglas de Negocio: La clave correcta es 'secreto'. Si la clave que escribiste es igual a la correcta, 
entraste. Si es diferente, suma 1 a tus intentos fallidos.

Restricciones: Usa un bloque `if/else`. Como en este caso la clave está mal, 
imprime exactamente: `'Intentos fallidos: '` seguido del número de intentos.

Resultado esperado en consola:
Intentos fallidos: 1
"""


clave_correcta = "secreto"
clave_incorrecta = "Admin123"
intentos_fallidos = 0

if clave_incorrecta == clave_correcta:
    print("Acceso habilitado")

else:
    intentos_fallidos += 1
print(f"Intentos fallidos: {intentos_fallidos}")