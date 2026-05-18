monto_retiro = 37000
billetes = [20000, 10000, 5000, 1000]
resultado_vuelto = {}
for billete in billetes:
    cantidad = monto_retiro // billete
    resultado_vuelto[billete] = cantidad
    monto_retiro = monto_retiro % billete

print(resultado_vuelto)
