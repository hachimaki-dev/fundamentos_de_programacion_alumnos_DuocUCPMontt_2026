servidor = 16
SO = 2.5
programa = 1.2



total_programas = programa*4

total_gasto = total_programas + SO

total_restante = servidor - total_gasto

total_restante_MB = total_restante*1024

print(total_restante_MB)