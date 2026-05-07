saldo = 50000
limite_diario = 200000
retiro = 60000

if retiro > limite_diario:
    print('Excede límite diario')
elif retiro > saldo:
    print('Saldo insuficiente')
elif retiro % 5000 != 0:
    print('Monto inválido')
else:
    print('Retiro exitoso')