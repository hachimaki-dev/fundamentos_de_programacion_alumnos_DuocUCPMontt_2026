# Tienes un diccionario llamado ventas, donde:

#    la clave es el nombre del producto
#    el valor es el monto vendido

# Debes recorrer el diccionario y sumar todos los valores.

# El resultado debe guardarse en total_ventas.

ventas = {
    "prod1": 50,
    "prod2": 100,
    "prod3": 250,
    "prod4": 10,
    "prod5": 25,
    "prod6": 600,
    "prod7": 800,
    "prod8": 1500,
    }

total_ventas = 0

for valor in  ventas.values():
    total_ventas += valor

print(total_ventas)