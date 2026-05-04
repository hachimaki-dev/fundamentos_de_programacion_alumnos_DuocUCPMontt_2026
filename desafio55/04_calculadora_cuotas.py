# Ejercicio 4: Calculadora de Cuotas (MercadoLibre)
# Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.
# Datos Iniciales: El notebook cuesta 1200000 y lo compraste en 12 cuotas sin interés. El envío a tu casa cuesta 15000.
# Reglas de Negocio: El envío no se paga en cuotas, se cobra completo junto con la primera cuota mensual del notebook.
# Restricciones: Calcula el valor de la cuota y súmale el envío. Imprime solamente el total que deberás pagar ese primer mes.

valor_notebook = 1200000
cuotas_sin_interes = 12
valor_envio = 15000

primera_cuota = (valor_notebook/cuotas_sin_interes) + valor_envio
print(primera_cuota)