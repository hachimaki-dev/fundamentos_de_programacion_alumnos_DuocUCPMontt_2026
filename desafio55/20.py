mi_saldo = 50000

limite_diario = 200000

quiero_retirar = 60000

multiplos = 5000

if quiero_retirar > limite_diario:
    print("Excede limite diario.")
elif quiero_retirar > mi_saldo:
    print("Saldo insuficiente.")
elif quiero_retirar % multiplos != 0:
    print("Monto invalido")
else:
    print("Retiro exitoso")
