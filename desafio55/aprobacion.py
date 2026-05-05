#Revisa si un cliente cumple los requisitos del banco para pedir un crédito.

#Datos Iniciales: El cliente tiene un sueldo de 550000 y tiene 1 deuda activa.

#Reglas de Negocio: El banco exige DOS cosas a la vez: que el sueldo sea mayor a 500000 Y que la cantidad de deudas sea exactamente 0.

#Restricciones: Usa la palabra reservada `and` dentro de un `if` para revisar ambas cosas en la misma línea. Imprime `'Aprobado'` o `'Rechazado'`.
cliente_saldo = 550000
deuda_activa = 1
if cliente_saldo > 500000 and deuda_activa == 0:
    print("aprobado")
elif cliente_saldo > 500000 and deuda_activa == 1:
    print("rechazado")

