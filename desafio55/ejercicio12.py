#Revisa si un cliente cumple los requisitos del banco para pedir un crédito.
#Datos Iniciales: El cliente tiene un sueldo de 550000 y tiene 1 deuda activa.
#Reglas de Negocio: El banco exige DOS cosas a la vez: que el sueldo sea mayor a 500000 Y que la cantidad de deudas sea exactamente 0.
#Restricciones: Usa la palabra reservada `and` dentro de un `if` para revisar ambas cosas en la misma línea. Imprime `'Aprobado'` o `'Rechazado'`.

sueldo = 550000
deudas = 1
if sueldo > 500000 and deudas == 0:
    print("aporbado")
else:
    print("Rechazado")