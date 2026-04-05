saldo_fijo=50000
pin_secreto=1357
intentos=1

while intentos<=3:
    pin_ingresado= int(input("Ingrese su PIN: "))
    if pin_ingresado!=pin_secreto:
        intentos+=1
    elif pin_ingresado==pin_secreto: 
        while pin_ingresado==pin_secreto:
            dinero_a_retirar=int(input("Cuanto dinero desea retirar: "))
            if dinero_a_retirar>saldo_fijo:
                print("Fondos insuficientes")
            elif dinero_a_retirar==0:
                print("Monto inválido")
            elif dinero_a_retirar<=saldo_fijo:
                saldo_fijo-= dinero_a_retirar
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo_fijo}")
                
print("Tarjeta bloqueada por seguridad")