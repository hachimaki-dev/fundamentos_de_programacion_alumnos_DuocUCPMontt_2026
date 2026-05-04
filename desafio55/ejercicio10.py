estacionamiento_valor_primera_hora = 1200
contador_primera_hora = 1
media_hora_extra = 500
contador_media_hora_extra = 4
horas_totales_estacionado = 3

media_hora_total = media_hora_extra * contador_media_hora_extra
primera_hora_total = estacionamiento_valor_primera_hora * contador_primera_hora
total_a_pagar = primera_hora_total + media_hora_total
print(total_a_pagar)

