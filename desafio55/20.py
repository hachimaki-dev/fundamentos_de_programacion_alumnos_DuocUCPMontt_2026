saldo = 50000
monto_limite = 200000
retiro = 60000

if retiro > monto_limite:
    print("Excede límite diario")

elif retiro > saldo:
    print("Saldo insuficiente")

elif retiro % 5000 != 0:
    print("Mondo Inválido")

else:
    print("Retiro exitoso")