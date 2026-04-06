saldo = 400000
contraseña_cuenta = 1010
n_intentos = 1
contraseña_ingresada = 0
saldo_a_retirar = 0

while n_intentos <= 3:
    contraseña_ingresada = int(input("Ingrese la contraseña de la cuenta: "))
    if contraseña_ingresada != contraseña_cuenta:
        print("La contraseña ingresada no es correcta")
        n_intentos = n_intentos + 1
        if n_intentos == 4:
            print("Tarjeta bloqueada por seguridad")
    elif contraseña_ingresada == contraseña_cuenta:
        saldo_a_retirar = int(input("Bienvenido, ¿Cuanto dinero desea retirar? "))
        if saldo_a_retirar > saldo:
            print("Fondos insuficientes")
            break
        elif saldo_a_retirar == 0:
            print("Monto invalido")
            break
        elif saldo_a_retirar < saldo:
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo - saldo_a_retirar}")
            break

