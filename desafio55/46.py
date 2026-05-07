ganancias_locales = {
    'LocalA': 150, 
    'LocalB': 300, 
    'LocalC': 100
    }
suma = 0

for valor in ganancias_locales.values():
    suma += valor

print(suma)