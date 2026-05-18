estacionamiento=1200
hora_extra=500
tiempo_total_que_estuviste=3

horas_estacionados=(tiempo_total_que_estuviste - 1)

bloque_extra=horas_estacionados*2

estacionamiento_a_pagar=estacionamiento + (bloque_extra * hora_extra)

print(estacionamiento_a_pagar)