saldo = 50000
limite_diario = 200000
retirar = 60000

if retirar > limite_diario:
    print("Excede límite diario")
elif retirar > saldo:
    print("Saldo insuficiente")
elif retirar % 5000 != 0:
    print("Monto inválido")
else:
    print("Retiro exitoso")