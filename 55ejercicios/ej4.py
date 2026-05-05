# Ejercicio 4: Calculadora de Cuotas (MercadoLibre)

print("============================================================")
print("Mercado Libre, la mejor App de compra y Envios de todo Chile")
print("============================================================")

precio_notebook = 1200000
cuotas = 12
envio = 15000

valor_cuotas = precio_notebook / cuotas
primer_pago = valor_cuotas + envio

print("El valor es", primer_pago)