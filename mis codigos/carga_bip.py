saldo_tarjeta = 10000
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000

saldo_actual = saldo_tarjeta - pasaje_micro

print(f"Este es su saldo actual despues de el primer viaje en micro.\n :{saldo_actual} \n")

saldo_actual_2 = saldo_tarjeta - (pasaje_metro * 2) - pasaje_micro

print(f"Este es el saldo actual despues de tomar los dos metros \n :{saldo_actual_2}\n")

saldo_actual_3 = saldo_tarjeta - (pasaje_metro * 2) - pasaje_micro + recarga

print(f"Este es el saldo actual despues de la recarga al final del dia \n :{saldo_actual_3}")