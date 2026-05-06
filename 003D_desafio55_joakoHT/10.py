primera_hora = 1200
costo_media_hora = 500
horas_totales = 3

horas_extra = horas_totales - 1
bloques_media_hora = horas_extra * 2

costo_total = primera_hora + (bloques_media_hora * costo_media_hora)

print(costo_total)