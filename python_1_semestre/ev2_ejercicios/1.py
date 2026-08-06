""" Servicio de Energía Eléctrica
Desarrolle un programa en Python que calcule el valor final 
de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio 
de medición.

Valores base:
Cuenta mensual: $45.000
Cargo de medición: $6.000
Reglas:
Si el consumo es mayor o igual a 500 kWh:
Tarifa A o B → 20% descuento
Tarifa C o D → 14% descuento
Si el consumo está entre 200 y 499 kWh:
Tarifa A o B → 12% descuento
Tarifa C o D → 8% descuento
Si el consumo es menor a 200 kWh → sin descuento.
Cargo de medición:
Tarifa A o B → 10% descuento.
Si además el consumo es mayor o igual a 400 kWh → 5% adicional."""

valor_final_energia = 0
valor_final_cargo_medicion = 0

cuenta_mensual = 45000
cargo_medicion = 6000

if consumo >= 500:
    tarifaA = tarifaA -(cuenta_mensual * 0.20)
    tarifaB = tarifaB -(cuenta_mensual * 0.20)
    tarifaC = tarifaC -(cuenta_mensual * 0.14)
    tarifaD = tarifaD -(cuenta_mensual * 0.14)

elif consumo >= 200 and consumo <= 499:
