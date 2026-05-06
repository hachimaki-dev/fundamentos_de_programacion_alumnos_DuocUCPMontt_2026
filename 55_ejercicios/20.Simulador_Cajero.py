saldo = 50000
limite_diario_retiro = 200000
retiro = 60000

if retiro > limite_diario_retiro:
    print("Excede limite diario")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro % 5000 != 0:
    print("Monto invalido")
else:
    print("Retiro exitoso")