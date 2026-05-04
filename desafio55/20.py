saldo = 50000
limite_diario_retiro = 200000
monto_a_retirar = 60000

if monto_a_retirar > limite_diario_retiro:
    print("Excede límite diario")
elif monto_a_retirar > saldo:
    print("Saldo insuficiente")
elif (monto_a_retirar % 5000) != 0:
    print("Monto inválido: El cajero no da monedas")
else:
    print("Retiro exitoso")
