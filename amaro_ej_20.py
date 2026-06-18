saldo = 50000
limite_dias = 200000
retiro = 60000

if retiro > limite_dias:
    print("Excede limite diario")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro % 5000 != 0:
    print("Monto inválido")
else:
    print("Retiro exitoso")