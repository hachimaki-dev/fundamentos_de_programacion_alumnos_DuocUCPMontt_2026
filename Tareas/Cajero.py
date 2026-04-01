saldo = 50.000
intentos_restantes = 3
pin = 2408
bandera = True
print("Bienvenido a el Banco Python, para ingresar necesitamos que dicte su pin")
print("Recuerde que el pin es de 4 DIGITOS")

while bandera:
    codigo_ingresado = input("Ingrese pin")
    if codigo_ingresado != pin:
        intentos_restantes = intentos_restantes - 1
        print(f"Pin incorreto, solamente tiene {intentos_restantes} intentos")