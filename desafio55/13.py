#jercicio 13: Promoción VIP BancoEstado (OR y AND)#
#evisa si un cliente puede subir a categoría VIP en su banco.
#
#atos Iniciales: El cliente gana 800000, lleva 6 años en el banco y tiene 0 deudas.
#
#eglas de Negocio: Eres VIP si cumples UNA de estas dos opciones:
#  Opción A) Ganas más de 1000000. Opción B) Llevas 5 o más años en el banco Y tienes 0 deudas.
#
#estricciones: Combina `or` y `and` en un mismo `if`. 
# Usa paréntesis para agrupar la Opción B y que Python no se confunda. Imprime `'Cliente VIP'`
#  o `'Cliente Normal'`.
#
#esultado esperado en consola:
#liente VIP


sueldo_cliente = 800000
antiguedad_banco = 6
deudas_cliente = 0


if (sueldo_cliente >= 1000000) and (antiguedad_banco >= 5) or (deudas_cliente == 0):
    print("Cliente VIP")

else:
    ("cliente normal")
