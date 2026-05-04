#Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.
#Datos Iniciales: El notebook cuesta 1200000 y lo compraste en 12 cuotas sin interés. El envío a tu casa cuesta 15000.
#Reglas de Negocio: El envío no se paga en cuotas, se cobra completo junto con la primera cuota mensual del notebook.
#Restricciones: Calcula el valor de la cuota y súmale el envío. Imprime solamente el total que deberás pagar ese primer mes.
costo_notebook = 1200000
costo_envio = 15000
cuotas = 12
cuota_mensual = costo_notebook / cuotas
print(cuota_mensual + costo_envio)