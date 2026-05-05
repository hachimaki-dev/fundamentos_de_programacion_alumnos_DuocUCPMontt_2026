# GB
total_gb = 16
sistema_operativo_gb = 2.5
programas = 4
consumo_programas_gb = 1.2

#GB a MB (1gb son 1024mb)
total_mb = total_gb * 1024
sistema_operativo_mb = sistema_operativo_gb * 1024
consumo_programas_mb = programas * consumo_programas_gb * 1024

suma_consumos = sistema_operativo_mb + consumo_programas_mb
total_restante = total_mb - suma_consumos 
print(f"total restante de memoria es: {total_restante}")
