saldo = 50000
limite_maximo_diario = 200000
retiro = 60000

if retiro > limite_maximo_diario:
    print("Excede límite diario")

elif retiro > saldo:
    print("Saldo insuficiente")

elif retiro % 5000 != 0:
    print("el cajero no da monedas")

else:
    print("retiro exitoso")