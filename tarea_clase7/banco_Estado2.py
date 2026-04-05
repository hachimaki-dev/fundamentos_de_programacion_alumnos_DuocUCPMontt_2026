saldo = 500000
PIN = 1604
NUMERO_MAXIMO_INTENTOS = 3

print("************************************")
print("****BIENVENIDO*A*BANCO*ESTADO*🦆****")
print("************************************")

while True:

    CLAVE_SECRETA = int(input("Por favor ingrese su clave secreta: "))

    if CLAVE_SECRETA == PIN :
        print("Has accedido")
    elif CLAVE_SECRETA != PIN :
        NUMERO_MAXIMO_INTENTOS -= 1
        print(f"No has accedido, Te quedan {NUMERO_MAXIMO_INTENTOS} intentos.")
    else:
        print("Ingrese un valor valido.")

    if NUMERO_MAXIMO_INTENTOS == 0:
        break

print("Eres boliviano, tu tarjeta ha sido bloqueada.")
