intentos_fallidos = 0
clave_user = input("ingrese clave")
if clave_user != "secreto":
    while clave_user != "secreto":

        intentos_fallidos += 1
        print(f"intentos fallidos {intentos_fallidos}")
        clave_user = input("ingrese clave")
else:
    print("correto")