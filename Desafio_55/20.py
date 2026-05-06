tu_saldo = 50000
limite_diario_de_retiros = 200000
quiero_retirar = 60000

if quiero_retirar > limite_diario_de_retiros:
    print("Excede el limite diario")
elif quiero_retirar > tu_saldo:
    print("Saldo insuficiente")
elif quiero_retirar != quiero_retirar % 5000 == 0:
    print("Monto invalido")
else:
    print("Retiro exitoso")