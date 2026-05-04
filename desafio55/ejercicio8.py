print("Ejercico 8: Rendimiento de servidor (AWS EC2)")

ram_total = 16
uso_so = 2.5
programas_corriendo = 1.2 * 4
consumo_ram = 0
consumo_ram = consumo_ram + uso_so + programas_corriendo
print(consumo_ram)
gb_libres = ram_total - consumo_ram
print(f"En total quedan {gb_libres * 1024} mb de ram libres.")