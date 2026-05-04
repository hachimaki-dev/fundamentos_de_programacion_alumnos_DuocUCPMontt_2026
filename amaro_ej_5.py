tarjeta = 10000
bus = 730
metro = 850
recarga = 3000

viaje = tarjeta - bus - (metro * 2)
saldo_final = viaje + recarga

print(f"Saldo final del día: ${saldo_final}")