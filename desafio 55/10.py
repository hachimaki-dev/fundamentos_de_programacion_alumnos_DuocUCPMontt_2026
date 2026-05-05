estacion = 1200
hora_extra = 500 
horas_totales = 3
horas_extra = horas_totales - 1
bloques_media_hora = horas_extra * 2


costo_primera_hora = estacion
costo_extras = bloques_media_hora * hora_extra
costo_total = costo_primera_hora + costo_extras

print(f"costo total a pagar: {costo_total}")
