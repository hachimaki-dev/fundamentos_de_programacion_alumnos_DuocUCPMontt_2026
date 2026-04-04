"""
Objetivo: Calcular el total a pagar de un pedido de comida, con descuentos.

1. Pregunta al usuario cuántos platos desea pedir (cantidad).
2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
4. Una vez terminado el ciclo, evalúa el subtotal con un if:
- Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".
- Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra: "Subtotal: $X, Envío: $2000, Total a pagar: $Z".
"""
import time

Preciototal = 0
preciototal_platos = 0
indicador_de_que_numero_de_plato_es = 1
platos = int(input("Cuantos platos deseas pedir? "))
while platos > 0:
    time.sleep(1)
    Precio = int(input(f"Cuanto va a costar el plato {indicador_de_que_numero_de_plato_es}? "))
    print(f"Plato {indicador_de_que_numero_de_plato_es} cuesta ${Precio}")
    indicador_de_que_numero_de_plato_es = indicador_de_que_numero_de_plato_es + 1
    platos = platos - 1
    preciototal_platos = preciototal_platos + Precio

if preciototal_platos > 15000:
    Preciototal = preciototal_platos * 0.9
    Descuento = preciototal_platos * 0.1
    time.sleep(1)
    print(f"Subtotal: ${preciototal_platos}, Descuento: ${Descuento}, Total pagar: ${Preciototal}")
elif preciototal_platos <= 15000 and preciototal_platos >= 0:
    Preciototal = preciototal_platos + 2000
    time.sleep(1)
    print(f"Subtotal: ${preciototal_platos}, Envío: $2000, Total a pagar: ${Preciototal}")