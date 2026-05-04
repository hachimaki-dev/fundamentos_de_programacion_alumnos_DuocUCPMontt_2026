saldo=50000 
limite=200000
retiro=60000
if limite<retiro:
    print("Excede limite diario")
elif retiro>saldo:
    print("saldo insuficiente")
else:
    print("Retiro exitoso")