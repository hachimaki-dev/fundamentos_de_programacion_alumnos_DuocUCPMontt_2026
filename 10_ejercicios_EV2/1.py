"""
Ejercicio 1: Servicio de Energía Eléctrica
MEDIUM
Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica 
y el valor final del cargo por servicio de medición.

Valores base:

Cuenta mensual: $45.000
Cargo de medición: $6.000
Reglas de descuento para la cuenta:

Si el consumo es mayor o igual a 500 kWh:
Tarifa A o B → 20% descuento
Tarifa C o D → 14% descuento
Si el consumo está entre 200 y 499 kWh:
Tarifa A o B → 12% descuento
Tarifa C o D → 8% descuento
Si el consumo es menor a 200 kWh → sin descuento.
Reglas para el cargo de medición:

Tarifa A o B → 10% descuento.
Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
Debe mostrar ambos valores finales.
"""

cta_mensual_base = 45000
cargo_medicion_base = 6000
total = cta_mensual_base + cargo_medicion_base
descuento_cuenta = 0
consumo = float(input("Ingresa tu consumo por favor: "))
tarifa = input("Ingrese su tarifa por favor (A, B, C, D): ").upper()

if consumo >= 500:
    if tarifa == "A" or tarifa == "B":
        descuento_cuenta = 0.20
    elif tarifa == "C" or tarifa == "D":
        descuento_cuenta = 0.14
elif consumo >= 200:
    if tarifa == "A" or tarifa == "B":
        descuento_cuenta = 0.12
    elif tarifa == "C" or tarifa == "D":
        descuento_cuenta = 0.08

valor_final_cuenta = cta_mensual_base * (1 - descuento_cuenta)

if tarifa == "A" or tarifa == "B":
    if consumo >= 400:
        valor_final_medicion = cargo_medicion_base * 0.90 * 0.95
    else:
        valor_final_medicion = cargo_medicion_base * 0.90
else:
    valor_final_medicion = cargo_medicion_base

print(f"Cuenta energia: {valor_final_cuenta}")
print(f"Cargo medicion: {valor_final_medicion}")
    


