#Cuenta mensual: $45.000
#Cargo de medición: $6.000
#Reglas de descuento para la cuenta:

#Si el consumo es mayor o igual a 500 kWh:
#Tarifa A o B → 20% descuento
#Tarifa C o D → 14% descuento
#Si el consumo está entre 200 y 499 kWh:
#Tarifa A o B → 12% descuento
#Tarifa C o D → 8% descuento
#Si el consumo es menor a 200 kWh → sin descuento.
#Reglas para el cargo de medición:

#Tarifa A o B → 10% descuento.
#Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
#Debe mostrar ambos valores finales.
cuenta_mensual = 45000
cargo_de_medicion = 6000
consumo = 600 
tarifa = "B"
if consumo >= 500:
    if tarifa == "A" or tarifa == "B":
        cuenta_mensual *= 0.8
    elif tarifa == "C" or tarifa == "D":
        cuenta_mensual *= 0.86
elif consumo >= 200 <= 499:
    if tarifa == "A" or tarifa == "B":
        cuenta_mensual *= 0.88
    elif tarifa == "C" or tarifa == "D":
        cuenta_mensual *= 0.92
elif consumo < 200:
    print("sin descuento")
if tarifa == "A" or tarifa == "B":
    cargo_de_medicion *= 0.90
    if consumo > 400:
        cargo_de_medicion *= 0.95
print(f"cuenta de energia {cuenta_mensual}")
print(f"cargo de medicion {cargo_de_medicion}")

