# Simulador de Cajero: Retiro Complejo

saldo = 50000 
limite_del_saldo = 200000
retiro = 60000

if retiro > limite_del_saldo:
    print('Excede limíte diario')
elif retiro > saldo:
    print('Saldo insuficiente')
elif saldo % 5000 !=0:
    print('Monto invalido')
else:
    print('Retiro exitoso')    
