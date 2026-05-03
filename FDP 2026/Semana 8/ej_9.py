# Tienes una lista llamada precios con varios números.

# Debes recorrerla con un ciclo for y sumar todos sus valores.

# El resultado debe guardarse en la variable total_pagar.

precios = [53,348,24,87,3,865,34]
total_pagar = 0

for precio in precios:
    total_pagar += precio

print(total_pagar)