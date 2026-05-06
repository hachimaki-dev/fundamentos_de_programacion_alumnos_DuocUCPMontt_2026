saldo = 50000
limite_diario = 200000  



saldo_retirado = int(input("ingresa el saldo que deseas retirar..."))

if saldo_retirado > 200000:
    print("Excede límite diario")
elif saldo_retirado > saldo:
    print("Saldo insuficiente")
elif saldo_retirado % 5000 != 0:
    print("el cajero no da monedas")
else:
    print("Retiro exitoso")

