# Ejercicio 12: Recorriendo un Diccionario
# Tienes un diccionario llamado ventas, donde:
#     la clave es el nombre del producto
#     el valor es el monto vendido
# Debes recorrer el diccionario y sumar todos los valores.
# El resultado debe guardarse en total_ventas.
# Pista: puedes usar .values() o .items().

ventas = {"producto1":1000, "producto2":2000, "producto3":3000}
total_ventas = 0

for valor in ventas.values():
    total_ventas += valor

print(total_ventas)