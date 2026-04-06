saldo = 50000
pin_secreto = "1234"
intentos = 0
max_intentos = 3

while intentos < max_intentos :
    pin_ingresado = input("Ingrese su PIN: ")
    if pin_ingresado == pin_secreto :
        print("PIN correcto. Bienvenido.")
        break
    else:
        intentos += 1
        print("PIN incorrecto. Intento", intentos, "de", max_intentos)
        if intentos == max_intentos :
            print("Tarjeta bloqueada por seguridad")
            exit()

monto = int(input("¿Cuánto dinero desea retirar?: "))
if monto > saldo :
    print("Fondos insuficientes")
elif monto == 0 :
    print("Monto inválido")
else:
    saldo -= monto
    print("Retiro exitoso. Su nuevo saldo es: $", saldo)