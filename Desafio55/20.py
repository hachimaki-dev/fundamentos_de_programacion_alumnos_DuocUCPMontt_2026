saldo=50000
limite_diario=200000
retiro=60000
if retiro>limite_diario:
    print("Excede límite diario")
elif retiro>saldo:
    print("Saldo Insuficiente")
elif retiro//5000!=0:
    print("Monto Invalido")
else:
    print("Retiro Exitoso")