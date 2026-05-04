"""
Ejercicio 4: Calculadora de Cuotas (MercadoLibre)
Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.

Datos Iniciales: El notebook cuesta 1200000 y lo compraste en 12 cuotas sin interés. El envío a tu casa cuesta 15000.

Reglas de Negocio: El envío no se paga en cuotas, se cobra completo junto con la primera cuota mensual del notebook.

Restricciones: Calcula el valor de la cuota y súmale el envío. Imprime solamente el total que deberás pagar ese primer mes.
"""

valor_notebook = 1200000 # 1,200,000
cantidad_cuotas = 12
envio_a_domicilio = 15000 # 15,000

print(f"Lo que debera pagar el primer mes es ${(valor_notebook/cantidad_cuotas) + envio_a_domicilio} con el envio incluido ($15000)")