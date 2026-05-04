intetos_fallidos=0
clave="secreto"
clave_usuario="Amin123"
clave_usuario=input("ingrese su clave ")
if clave_usuario == clave:
    print("Bienvenido")
else: 
    intetos_fallidos+=1
    print(f"intendos fallidos: {intetos_fallidos}")
