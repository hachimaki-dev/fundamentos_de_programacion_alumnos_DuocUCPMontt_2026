precio_notebook = 1200000
total_cuotas = 12
envio_casa = 15000

valor_couta = precio_notebook // total_cuotas
cobro_primer_mes = valor_couta + envio_casa

print(f"El total a pagar el primer mes es de: ${cobro_primer_mes}")