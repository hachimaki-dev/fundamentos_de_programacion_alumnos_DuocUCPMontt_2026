tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850

tarjeta = tarjeta - (pasaje_micro + (pasaje_metro * 2))
print(f"Al terminar el día 1, viajaste en 1 micro y en 2 metros, lo que hace un total de ${pasaje_micro + (pasaje_metro * 2)}, tu nuevo saldo es de: ${tarjeta}")
tarjeta += 3000
print(f"Al día 2, haces una recarga de $3000, por lo que tu nuevo saldo es de {tarjeta}")
