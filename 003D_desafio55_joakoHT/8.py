total_ram_gb = 16
ram_so = 2.5
ram_programas = 4 * 1.2

ram_usada = ram_so + ram_programas
ram_libre_gb = total_ram_gb - ram_usada

ram_libre_mb = ram_libre_gb * 1024

print(ram_libre_mb)