# Tienes:

#    una lista llamada compras, con nombres de productos comprados
#    un diccionario llamado precios, donde cada producto tiene su costo

# Debes calcular el total sumando el precio de cada producto comprado.

# Si el subtotal es mayor a 200, aplica un descuento del 10%.

# Guarda el resultado final en total_final.

compras = ["pan", "microondas", "pan"]

precios = {
    "pan": 50,
    "microondas": 150,
}

total_final = 0

for compra in compras:
    total_final += precios.get(compra)

if total_final > 200:
    total_final -= total_final * 0.1

print(f"Total: {total_final}")