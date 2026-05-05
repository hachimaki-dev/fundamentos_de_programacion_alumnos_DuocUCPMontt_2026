clave = "secreto"
intento_fallido = 0
clave_ingresada = "admin123"


if clave_ingresada == "secreto":
   print("puede ingresar")
else:
   print("clave incorrecta")
   intento_fallido = intento_fallido + 1
print("intentos fallidos: ", intento_fallido)