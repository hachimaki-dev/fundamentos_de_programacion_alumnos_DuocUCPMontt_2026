saldo = 50000
maximo_diario_retiro = 200000
retiro = 60000
if retiro > maximo_diario_retiro:
    print("Excede limite diario")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro % 5000 != 0:
    print("Monto invàlido")
else:
    print("Retiro exitoso")