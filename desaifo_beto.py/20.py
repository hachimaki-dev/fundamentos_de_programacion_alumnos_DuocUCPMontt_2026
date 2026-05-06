saldo = 50000
limite_diario = 200000
dinero_pedido = int(input("cuanto dinero quieres sacar"))

if dinero_pedido > saldo:
    print("saldo insuficiente")
elif dinero_pedido > saldo:
    print("Saldo insuficiente")
elif dinero_pedido %5000 != 0:
    print("monto invalido")
else:
    print("retiro exitoso")