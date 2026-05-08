#Tienes 50000 de saldo.
#limite máximo diario para sacar plata es 200000.
#Quieres retirar 60000

saldo = 50000
limite_maximo = 200000
retirar = int(input("Ingresa monto a retirar: "))

if saldo > retirar:
    print("Excede límite diario")
elif saldo < retirar:
    print("Saldo insuficiente")
else:
    print("Retiro exitoso")