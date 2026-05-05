saldo = 50000 
limite_max_retiro = 200000
retiro = 60000
if retiro > limite_max_retiro:
    print("Excede el limite")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro % 5000 != 0:
    print("Monto Invalido")
else:
    print("Retiro exitoso")