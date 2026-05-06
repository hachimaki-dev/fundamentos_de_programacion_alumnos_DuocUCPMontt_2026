saldo = 50000
limite_diario = 200000
monto_retirado = 60000

if monto_retirado > limite_diario:
    print("excede limite diario")
elif monto_retirado > saldo:
    print("saldo insuficiente")
elif monto_retirado % 5000 != 0:
    print("monto invalido")
else:
    print("retiro exitoso")
    