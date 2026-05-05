
saldo = 50000
limite_diario_retiro = 200000
quiero_retirar = 60000
if quiero_retirar %5000 == 0:
    if quiero_retirar > limite_diario_retiro:
        print("--excede limite diario--")
    elif quiero_retirar > saldo :
        print("--saldo insuficiente--")
    else:
        print("--retiro exitoso--")
else:
    print("--monto invalido--")

