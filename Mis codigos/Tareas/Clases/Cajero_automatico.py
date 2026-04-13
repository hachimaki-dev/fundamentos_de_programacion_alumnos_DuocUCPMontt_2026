saldo = 50000
intentos_fallidos = 0
pin = 1604
numero_maximo_intentos = 3
contador_intentos_fallidos = 0

print("****BIENVENIDOS A BANCO ESTADO****")

while True:
    pin_ingresado = int(input("Por favor, ingrese su clave secretita"))

    if pin_ingresado == pin :
        print("Haz accedido")
        break
        
    elif pin_ingresado != pin :
        contador_intentos_fallidos = contador_intentos_fallidos + 1
        print("No haz accedido")
    else:
        print("Ingrese una contraseña vàlida")
    if contador_intentos_fallidos >= 3:
        break





