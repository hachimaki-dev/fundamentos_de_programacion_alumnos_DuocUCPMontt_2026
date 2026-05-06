# Ejercicio 10: Estacionamiento Aeropuerto

print("===================================================")
print("Bienvenido al sistema de cálculo de estacionamiento")
print("===================================================")

precio_primera_hora = 1200
precio_media_hora = 500

horas_totales = 3
horas_extra = horas_totales - 1

bloques_media_hora = horas_extra * 2

costo_extra = bloques_media_hora * precio_media_hora

costo_total = precio_primera_hora + costo_extra

print(costo_total)