saldo = 50000
limite = 200000
retirar = 60000
multiplo = 5000
if retirar > limite:
    print("excede limite diario")
elif retirar > saldo:
    print("saldo insuficiente")
elif retirar % multiplo != 0:
    print("no es multiplo")
else:
    print("retiro exitoso")