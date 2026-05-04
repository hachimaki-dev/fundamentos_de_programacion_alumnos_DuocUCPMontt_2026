saldo = 50000
lim_diario = 200000
monto_retirar = 60000

if monto_retirar > lim_diario:
    print("Excede limite diario")
elif monto_retirar > saldo:
    print("Saldo insuficiente")
elif monto_retirar % 5000 == 0:
    print("Monto inválido")
else:
    print("Retiro exitoso")