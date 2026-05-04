costo_estacionamiento_por_hora = 1200
costo_media_hora_extra = 500

horas_estacionado = 3

cantidad_hora_cobrada = 1
cantidad_media_hora_extra_cobradas = 4

precio_total = (cantidad_hora_cobrada * costo_estacionamiento_por_hora) + (cantidad_media_hora_extra_cobradas * costo_media_hora_extra)

print(precio_total)