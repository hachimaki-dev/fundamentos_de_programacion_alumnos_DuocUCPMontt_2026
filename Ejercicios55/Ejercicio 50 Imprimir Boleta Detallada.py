# Ejercicio 50: Imprimir Boleta Detallada

# El Mini-Boss: Sácale la información a un diccionario para armar una boleta real de restaurante.

# Datos Iniciales: La cuenta es: `{'Papas': 5000, 'Pizza': 10000}`.

# Reglas de Negocio: Tienes que sumar el total de los platos. Una vez sumado, tienes que calcular el 10% extra por la propina y sumárselo al total final.

# Restricciones: Usa la herramienta `.items()` en un ciclo `for` para extraer la pareja completa (el nombre del plato y el precio) al mismo tiempo. Haz la matemática e imprime `'Total final: '` junto al número final con propina.

menu = {"Papas": 5000, "Pizza": 10000}
total = 0

for plato, precio in menu.items():
    total += precio

propina = total * 0.10

total_final = total + propina

print(f"Total final: {total_final}")