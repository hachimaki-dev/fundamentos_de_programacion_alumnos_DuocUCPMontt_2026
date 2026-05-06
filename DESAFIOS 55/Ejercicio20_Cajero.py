saldo=50000
limitediario=200000
retiro=60000

if retiro > limitediario:
    print ('Excede límite diario')
elif retiro > saldo:
    print ('Saldo Insuficiente')
elif abs(retiro % 5000) > 0:
    print ('Monto Invalido')
else:
    print('Retiro exitoso')
    saldo= saldo - retiro