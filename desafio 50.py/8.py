total_ram=16
sistena_operativo=2.5
cantidad_programas=4
comsumo_programa=1.2

gasto_total= cantidad_programas * comsumo_programa

comsumo_total=sistena_operativo + gasto_total

ram_libre_gb=total_ram - comsumo_total

resultado_final= ram_libre_gb * 1024

print(resultado_final)