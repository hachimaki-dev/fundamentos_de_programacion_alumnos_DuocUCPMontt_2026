valor_primera_hora = 1200
valor_media_hora = 500
horas_estacionado = 3
horas_extra = horas_estacionado - 1
bloque_extra = horas_extra * 2
total = valor_primera_hora + (bloque_extra * valor_media_hora)
print(total)