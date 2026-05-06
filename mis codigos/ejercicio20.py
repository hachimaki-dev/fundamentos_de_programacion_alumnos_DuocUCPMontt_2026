tienes = 50000
limite = 200000
retirar = 60000
if retirar  > limite:
    print("Excede limite diario")

elif retirar > tienes:
    print("Saldo insuficiente")

elif retirar % 5000 != 0:
    print("Monto invalido")

else:
    print("Retiro exitoso")