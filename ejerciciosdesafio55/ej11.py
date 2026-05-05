intento_fallidos = 0
clave_ingresada = "admin123"
clave_correcta = "secreto"

if clave_ingresada == clave_correcta:
    print("entraste")
else: 
    intento_fallidos = intento_fallidos + 1
    print("intento_fallido" , intento_fallidos)