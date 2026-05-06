intentos_fallidos = 0
clave = 1234

while True:
    clave_ingresada = int(input("Por favor, ingrese su clave, recuerde que esta es de 4 digitos"))
    if clave_ingresada == clave:
        print("Accediendo al sistema")
        print("Haz accedido con exito")
    else:
        intentos_fallidos = intentos_fallidos + 1
        print(f"CLAVE INCORRECTA, TE QUEDAN {(intentos_fallidos - 3) * -1} INTENTOS")
        if intentos_fallidos == 3:
            print("BLOQUEANDO SISTEMA")
            import sys
            sys.exit()
            