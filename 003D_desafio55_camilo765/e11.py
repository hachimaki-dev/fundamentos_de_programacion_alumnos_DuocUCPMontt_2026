intentos_fallidos = 0
clave_ingresada = 'Admin123'
clave_correctax = 'secreto'

if clave_ingresada == clave_correcta:
    print("Entraste")
else:
    intentos_fallidos += 1
    print('Intentos fallidos: ' + str(intentos_fallidos))
