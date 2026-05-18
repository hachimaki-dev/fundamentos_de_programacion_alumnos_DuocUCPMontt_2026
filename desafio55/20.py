saldo = 50000
limite_Diario = 200000
monto_retiro = 60000
if monto_retiro > limite_Diario:
    print("Excede limite diario")
elif monto_retiro > saldo:
    print("Saldo insuficiente")
elif monto_retiro % 5000 != 0:
    print("Monto invalido")
else:
    print("Retiro exitoso")