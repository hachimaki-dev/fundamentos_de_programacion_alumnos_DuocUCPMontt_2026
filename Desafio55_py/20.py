saldo = 50000
limite_diario = 200000
quieres_retirar = 60000

if quieres_retirar > limite_diario:
    print("EXCEDE LIMITE DIARIO")
elif quieres_retirar > saldo:
    print("SALDO INSUFICIENTE")
elif quieres_retirar % 5000 != 0:
    print("MONTO INVALIDO")
else:
    print("RETRO EXITOSO")