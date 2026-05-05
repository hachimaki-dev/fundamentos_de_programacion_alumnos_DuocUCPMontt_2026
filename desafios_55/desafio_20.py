saldo = 50000 
limite_diario = 200000
monto_a_retirar = 60000

if monto_a_retirar > limite_diario:
    print("Excede limite diario")

elif monto_a_retirar > saldo:
    print("Saldo insuficiente")
    
elif monto_a_retirar % 5000 != 0:
    print("Monto invalido")

else:
    print("Retiro exitoso")