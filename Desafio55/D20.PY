saldo = 50000
retiro_maximo = 200000
retiro = 40000
if retiro > retiro_maximo:
    print("excede limite diario")
elif retiro > saldo:
    print("saldo insuficiente")
elif (retiro % 5000) > 0:
    print("monto invalido")
else:
    print("retiro exitoso")
