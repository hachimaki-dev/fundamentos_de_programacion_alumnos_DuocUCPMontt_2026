#Ejercicio 11: Clave Única Básico
#Simula el ingreso a tu cuenta con una clave secreta.

#Datos Iniciales: Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave #'Admin123'.

#Reglas de Negocio: La clave correcta es 'secreto'. Si la clave que escribiste es igual a la #correcta, entraste. Si es diferente, suma 1 a tus intentos fallidos.

#Restricciones: Usa un bloque `if/else`. Como en este caso la clave está mal, imprime #exactamente: `'Intentos fallidos: '` seguido del número de intentos.


clave_de_acceso = 'Admin123'
intentos_fallidos = 0


while clave_de_acceso != "secreto":
    intentos_fallidos += 1
    clave_de_acceso = input("Ingrese la clave de acceso: ")


if clave_de_acceso == 'Admin123':
    print(f"acceso permitido {intentos_fallidos} en intentos")
else:
    print(f"acceso denegado {intentos_fallidos} en intentos")
    intentos_fallidos += 1


