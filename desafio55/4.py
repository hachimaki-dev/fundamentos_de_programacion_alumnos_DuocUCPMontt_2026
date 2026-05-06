"""
Ejercicio 4: Calculadora de Cuotas (MercadoLibre)
Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.

Datos Iniciales: El notebook cuesta 1200000 y lo compraste en 12 cuotas sin interés.
El envío a tu casa cuesta 15000.

Reglas de Negocio: El envío no se paga en cuotas, se cobra completo junto con la primera 
cuota mensual del notebook.

Restricciones: Calcula el valor de la cuota y súmale el envío. Imprime solamente el total que 
deberás pagar ese primer mes.

Resultado esperado en consola:
115000.0
"""

valor_notebook = 1200000
cuotas = 12
envio = 15000

valor_cuotas = valor_notebook / cuotas

costo_envio = envio + valor_cuotas

print(f"El total que debera pagar es de: ${costo_envio}")
