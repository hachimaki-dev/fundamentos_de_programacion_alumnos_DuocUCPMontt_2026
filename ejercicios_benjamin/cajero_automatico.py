#datos iniciales 
saldo = 50000 
pin_correcto = 1234
intentos = 0 
acceso = False 

#Validación de pin
while intentos < 3:
    pin = int(input("Ingrese su PIN: "))

    if pin == pin_correcto:
        acceso = True
        break 
    else:
        intentos += 1
        print("PIN incorrecto.")
#verificar acceso 
if not acceso:
    print("tarjeta bloqueada por seguridad!") 
else:
    print("Acceso concedido.")

#menú de retiro 
retiro = int(input("Ingrese el monto a retirar: "))
if retiro > saldo:
    print("Fondos insuficientes.") 
elif retiro <= 0:
    print("Monto inválido.")
else:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")