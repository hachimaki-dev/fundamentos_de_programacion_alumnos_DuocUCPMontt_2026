saldo = 50000
PIN = 1290
numero_maximo_de_intentos = 3
contador_intentos_fallidos = 0
print("bienvenidos a banco estado")
while True :
    pin_ingresado = int(input("por favor ingrese su contraseña: "))

    if pin_ingresado == PIN :
        print("Haz accedido")
    elif  pin_ingresado != PIN :
        print("no haz accedido")
        contador_intentos_fallidos = contador_intentos_fallidos + 1
    else:
        print("ingresa la contraseña valida")

    if contador_intentos_fallidos >=3:
    
        break
        
print("fin del programa")



