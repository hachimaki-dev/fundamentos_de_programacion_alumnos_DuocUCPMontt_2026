# Ejercicio 9: Sumando una Lista
# Tienes una lista llamada precios con varios números.
# Debes recorrerla con un ciclo for y sumar todos sus valores.
# El resultado debe guardarse en la variable total_pagar.
# Ejemplo: Si precios = [1000, 2500, 500], entonces total_pagar = 4000.

precios = [1000, 2500, 500]
total_pagar = 0

for precio in precios:
    total_pagar += precio

print(total_pagar)