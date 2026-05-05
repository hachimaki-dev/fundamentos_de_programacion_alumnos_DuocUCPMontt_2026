# Ejercicio 8: Rendimiento de Servidor (AWS EC2)

print("Cálculo de memoria libre del servidor")
print("-------------------------------------")

ram_total = 16
sistema = 2.5
programas = 4
ram_por_programa = 1.2

uso_programas = programas * ram_por_programa

ram_usada = sistema + uso_programas

ram_libre = ram_total - ram_usada

ram_libre_mb = ram_libre * 1024

print(ram_libre_mb)