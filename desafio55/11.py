intentos_fallidos = 0
clave = "secreto"
clave_escrita = "Admin123"
if clave_escrita == clave:
    print ("entraste")
else:
    intentos_fallidos +=1
    print ("Intentos fallidos ",intentos_fallidos)
