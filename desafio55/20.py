Saldo = 50000
limite_diario = 200000
monto_retiro = 60000
if monto_retiro > limite_diario:
    print("Excede limite diario")
elif monto_retiro > Saldo:
    print("Saldo insuficiente")
elif monto_retiro % 5000:
    print("Monto invalido")
else: 
    print("Retiro exitoso")

