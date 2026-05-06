saldo = 50000
limite = 200000
retirar = 60000
if retirar > limite:
    print("excede limite diario")
elif retirar > saldo:
    print("saldo insuficiente")
elif retirar % saldo:
    print("monto invalido")
else:
    print("retiro exitoso")