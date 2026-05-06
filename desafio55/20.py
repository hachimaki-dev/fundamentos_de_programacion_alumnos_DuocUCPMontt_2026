saldo = 50000
maximo_retiro_diario = 200000
monto_a_retirar = 60000

if monto_a_retirar > maximo_retiro_diario:
    print("Excede limite diario")

elif monto_a_retirar > saldo:
    print("Saldo insuficiente")

elif monto_a_retirar % 5000:
    print("Monto invalido")

else:
    print("Retiro exitoso")