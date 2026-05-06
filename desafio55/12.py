#jercicio 12: Aprobación de Crédito (AND simple)#
#evisa si un cliente cumpl# los requisitos del banco para pedir un crédito.#
#Datos Iniciales: El cliente #iene un sueldo de 550000 y tiene 1 deuda activa.#
#Reglas de Negocio: El banco exige DOS cosas a la vez: que el sueldo sea mayor a 5000#0 
# 
#Y que la cantidad de deudas sea exactamente 0.#
#Restricciones: Usa la palabra reservada `and` 
# dentro de un `if` para revisar ambas cosas en la m#sma línea. Imprime `'Aprobado'` # `
# 'Rechazado#`.#
#Resultado esperado en consola:
# #rechazado
#
# 
#   


sueldo_cliente = 550000
deuda_activa = 1

if sueldo_cliente >= 500000 and deuda_activa == 0:
    print("Aprobado")

else:
    print("rechazado")



