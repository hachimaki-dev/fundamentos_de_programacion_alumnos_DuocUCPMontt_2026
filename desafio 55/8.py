ram_total = 16
ram_sistema = 2.5
programas = 4
ram_por_programa = 1.2

ram_usada = ram_sistema + (programas * ram_por_programa)
ram_libre_gb = ram_total - ram_usada
ram_libre_mb = ram_libre_gb * 1024

print(f"ram disponible en el servidor: {ram_libre_mb}")