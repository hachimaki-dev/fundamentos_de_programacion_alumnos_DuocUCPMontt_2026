intentos_fallidos = 0
clave_correcta = "secreto"
clave_escrita = "admin123"
if clave_escrita == clave_correcta:
    print("Acceso concedido")
else:
    intentos_fallidos += 1
    print("Intentos fallidos: ", intentos_fallidos)