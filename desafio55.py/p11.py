intentos_fallidos = 0
clave_incorrecta = "Admin123"
clave_correcta = "Secreto"
clave_escrita = ""

if clave_escrita == clave_correcta:
    print("Entraste")
else:
    intentos_fallidos = intentos_fallidos + 1
    print("Intentos fallidos:", intentos_fallidos)