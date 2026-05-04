Saldo_inicial = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

dinero_gastado = pasaje_micro + (pasaje_metro*2)
saldo_final = Saldo_inicial - dinero_gastado + recarga
print(f"el saldo final de la tarjeta es de ${saldo_final}")