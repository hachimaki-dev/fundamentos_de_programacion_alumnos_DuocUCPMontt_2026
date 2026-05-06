tarifa_primera_hora = 1200
tarifa_media_hora_extra = 500
tiempo_total_horas = 3

horas_extra = tiempo_total_horas - 1

bloques_extra = horas_extra * 2

costo_total = tarifa_primera_hora + (bloques_extra * tarifa_media_hora_extra)

print(costo_total)