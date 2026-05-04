clave_escrita = 'Admin123'
clave_correcta = 'secreto'
intentos_fallidos = 0
if clave_escrita == clave_correcta:
    print("acceso concedido")
else: 
    intentos_fallidos += 1
    print("intento fallido:", intentos_fallidos)
    