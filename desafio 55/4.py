notebook = 1200000
cuotas = 12
envio = 15000

cuota_mensual = notebook / cuotas
primer_mes = cuota_mensual + envio

print(f"total a pagar el primer mes: {primer_mes}")