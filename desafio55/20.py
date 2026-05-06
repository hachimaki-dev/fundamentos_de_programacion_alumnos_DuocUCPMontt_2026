saldo= 50000
retiro_maximo= 200000
monto_a_retirar= 60000

if monto_a_retirar > saldo:
    print("Saldo insuficiente")
elif monto_a_retirar > retiro_maximo:
    print("Excede monto maximo diario")
elif monto_a_retirar % 5000 == 0:
    print("Monto invalido")
else:
    print("Retiro exitoso")