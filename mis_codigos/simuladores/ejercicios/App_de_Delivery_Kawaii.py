# Pregunta al usuario cuántos platos desea pedir (cantidad).
cantidad = int(input("¿Cuántos platos desea pedir? "))
# Usa un ciclo while y un contador para pedir el precio de CADA plato.
contador = 0
total = 0
while contador < cantidad:
# Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
    precio_plato = float(input(f"Ingrese el precio del plato {contador + 1}: "))
    # Una vez terminado el ciclo, evalúa el subtotal con un if 
    if total > 15000: # Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle:
        descuento = total * 0.1 # "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
        total -= descuento
        print(f"Subtotal: ${total + descuento}, Descuento: ${descuento}, Total pagar: ${total}")
    else:
        print(f"Subtotal: ${total}, Descuento: $0, Total pagar: ${total}")# Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".
        total += 2000
    contador += 1       
    


