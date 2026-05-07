saldo = 50000
maximo = 200000
retiro = 60000
if retiro > maximo:
    print("Excede límite diario")
elif retiro > saldo:
    print("Saldo insuficiente")
elif retiro % 5000 != 0:
    print("Monto inválido")
else:
    print("Retiro Exitoso")