#🟡 Rango: Cuidado
#Ejercicio 13: Promoción VIP BancoEstado (OR y AND)
#Revisa si un cliente puede subir a categoría VIP en su banco.

#Datos Iniciales: El cliente gana 800000, lleva 6 años en el banco y tiene 0 deudas.

#Reglas de Negocio: Eres VIP si cumples UNA de estas dos opciones: Opción A) Ganas más de 1000000. Opción B) Llevas 5 o más años en el banco Y tienes 0 deudas.

#Restricciones: Combina `or` y `and` en un mismo `if`. Usa paréntesis para agrupar la Opción B y que Python no se confunda. Imprime `'Cliente VIP'` o `'Cliente Normal'`.

ganancia_cliente = 800000
vigencia_banco = 6
deudas_cliente = 0

ganancia_vip = 1000000
vigencia_vip = 5
deudas_vip = 0

if ganancia_cliente > ganancia_vip or vigencia_banco >=  vigencia_vip and deudas_cliente == deudas_vip :
    print("Ustedes puede optar a ser un cliente V.I.P")
else :
    print("Usted es un fracasado y no puede optar a nuestra membresía V.I.P")

