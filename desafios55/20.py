saldo = 50000
limite_diario = 200000
monto_retiro = 60000

if monto_retiro > limite_diario:
    
    print('Excede límite diario')

elif monto_retiro > saldo:
    
    print('Saldo insuficiente')

elif monto_retiro % 5000 != 0:
    
    print('Monto inválido')

else:

    saldo -= monto_retiro
    
    print('Retiro exitoso')