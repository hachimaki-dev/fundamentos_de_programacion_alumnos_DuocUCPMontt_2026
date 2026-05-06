saldo = 50000
limite_diario = 200000
retiro = 60000
if retiro > limite_diario:
    print("excede limite diario")
elif retiro > saldo:
    print("saldo insuficiente")
elif retiro % 5000 != 0:
    print("monto invalido")
else:
    print("retiro exitoso")
    