mi_saldo = 50000
limite_plata_diario = 200000
monto_a_retirar = 60000
if monto_a_retirar > limite_plata_diario:
    print("exede limite diario")
elif monto_a_retirar > mi_saldo:
    print("saldo insuficiente")
elif monto_a_retirar % 5000 != 0:
    print("monto invalido")
else:
    print("retiro exitoso")