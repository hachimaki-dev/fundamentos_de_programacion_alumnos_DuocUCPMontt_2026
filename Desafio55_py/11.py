intentos_fallidos = 0
clave = "secreto"

pregunta = input("INGRESE LA CONTRASEÑA:  ").lower
if pregunta == clave:
    print("ENTRASTE")
    intentos_fallidos =+ 1
    print(f"INTENTOS : {intentos_fallidos}")
else:
    print("INGRESE UNA CONTRASEÑA VALIDA")
    intentos_fallidos =+ 1
    print(f"INTENTOS : {intentos_fallidos}")