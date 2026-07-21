# Ejercicio 1: Servicio de Energía Eléctrica
# MEDIUM
# Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio de medición.

# Valores base:

# Cuenta mensual: $45.000
# Cargo de medición: $6.000

# Reglas de descuento para la cuenta:

# Si el consumo es mayor o igual a 500 kWh:
# Tarifa A o B → 20% descuento
# Tarifa C o D → 14% descuento
# Si el consumo está entre 200 y 499 kWh:
# Tarifa A o B → 12% descuento
# Tarifa C o D → 8% descuento
# Si el consumo es menor a 200 kWh → sin descuento.


# Reglas para el cargo de medición:
# Tarifa A o B → 10% descuento.
# Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
# Debe mostrar ambos valores finales.

# Input Esperado
# 600
# B
# Output Esperado
# Cuenta energia: 36000
# Cargo medicion: 5130

cuenta_mensual = 45000
cargo_de_medicion = 6000

consumo = int(input("¿Cuantos kWh consumiste en el mes?: "))
tipo_de_tarifa = input("¿Que tipo de plan de compañia tiene?  A, B ,C o D: ")


if consumo >= 500:
    if tipo_de_tarifa == "A" or tipo_de_tarifa == "B":
        descuento_mensual = cuenta_mensual * 0.80

    elif tipo_de_tarifa == "C" or tipo_de_tarifa == "D":
        descuento_mensual = cuenta_mensual * 0.86

elif consumo >= 200 and consumo <= 499:
    if tipo_de_tarifa == "A" or tipo_de_tarifa == "B":
        descuento_mensual = cuenta_mensual * 0.88

    elif tipo_de_tarifa == "C" or tipo_de_tarifa == "D":
        descuento_mensual = cuenta_mensual * 0.92


if tipo_de_tarifa == "A" or tipo_de_tarifa == "B":
    descuento_medicion = cargo_de_medicion * 0.90
elif tipo_de_tarifa == "C" or tipo_de_tarifa == "D":
    descuento_medicion = cargo_de_medicion

if tipo_de_tarifa == "A"and consumo >= 400 or tipo_de_tarifa == "B" and consumo >= 400:
    descuento_medicion -= descuento_medicion * 0.05
elif consumo < 200:
    descuento_mensual = cuenta_mensual

print(f"Cuenta energia: {int(descuento_mensual)}")
print(f"Cargo medicion: {int(descuento_medicion)}")



