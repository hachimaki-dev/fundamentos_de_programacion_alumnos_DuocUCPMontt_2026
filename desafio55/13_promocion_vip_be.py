# Ejercicio 13: Promoción VIP BancoEstado (OR y AND)
# Revisa si un cliente puede subir a categoría VIP en su banco.
# Datos Iniciales: El cliente gana 800000, lleva 6 años en el banco y tiene 0 deudas.
# Reglas de Negocio: Eres VIP si cumples UNA de estas dos opciones: Opción A) Ganas más de 1000000. Opción B) Llevas 5 o más años en el banco Y tienes 0 deudas.
# Restricciones: Combina `or` y `and` en un mismo `if`. Usa paréntesis para agrupar la Opción B y que Python no se confunda. Imprime `'Cliente VIP'` o `'Cliente Normal'`.

sueldo = 800000
cantidad_deudas = 0
anios_como_cliente = 6

if (sueldo > 1000000) or (anios_como_cliente > 5 and cantidad_deudas == 0):
    print("Cliente VIP")
else:
    print("Cliente Normal")