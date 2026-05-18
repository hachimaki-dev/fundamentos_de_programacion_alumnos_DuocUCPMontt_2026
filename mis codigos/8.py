RAM = 1024 * 16
sistema_operativo = 1024 * 2.5
programas = 1024 * 4

suma_RAM = sistema_operativo + programas
total_gb = suma_RAM - RAM

print(f"el espacio disponible en la RAM es de {total_gb} GB")

