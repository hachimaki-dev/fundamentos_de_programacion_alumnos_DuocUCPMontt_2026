tienes = 50000
limite_diario = 200000
quieres_retirar = 60000

if limite_diario > 200000 :
    print("Excede límite diario")
elif tienes >= 50000:
    print("Saldo insuficiente")
elif tienes < 50000:
    print("Monto inválido")
else:
    print("Retiro exitoso")