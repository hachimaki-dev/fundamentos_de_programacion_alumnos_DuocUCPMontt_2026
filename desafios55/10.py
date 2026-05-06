precio_primera_hora = 1200
precio_media_hora_extra = 500
horas_totales = 3

horas_extras = horas_totales - 1

bloques_media_hora = horas_extras * 2

costo_primera_hora = precio_primera_hora
costo_horas_extras = bloques_media_hora * precio_media_hora_extra
costo_total = costo_primera_hora + costo_horas_extras

print(f"El costo total de estacionamiento es de {costo_total}")