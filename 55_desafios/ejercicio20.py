saldo = 50000
limite_diario = 200000
retiro = 60000

if limite_diario > 200000:
    print("excede limite diario")

elif retiro > 50000:
    print("saldo insuficiente")

elif retiro % 5000 != 0:
    print("Monto inválido")

else:
    print("retiro exitoso")
