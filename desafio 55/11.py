intentos_fallidos = 0
clave_ingresada = 'Admin123'
clave_correcta = 'secreto'

if clave_ingresada == clave_correcta:
    print('Acceso concedido')
else:
    intentos_fallidos += 1
    print('Intentos fallidos:', intentos_fallidos)