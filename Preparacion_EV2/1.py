#Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio de medición.
#Valores base:
#    Cuenta mensual: $45.000
#    Cargo de medición: $6.000
#Reglas de descuento para la cuenta:
#    Si el consumo es mayor o igual a 500 kWh:
#        Tarifa A o B → 20% descuento
#        Tarifa C o D → 14% descuento
#    Si el consumo está entre 200 y 499 kWh:
#        Tarifa A o B → 12% descuento
#        Tarifa C o D → 8% descuento
#    Si el consumo es menor a 200 kWh → sin descuento.
#Reglas para el cargo de medición:
#    Tarifa A o B → 10% descuento.
#    Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
#Debe mostrar ambos valores finales.
cuenta_mensual =45000
cargo_de_medicion = 6000
consumo = int(input("Ingrese su consumo en kWh:\n"))
tarifa = input("ingrese su tarifa A,B,C,D\n")
if consumo >= 500:
    if tarifa == "A" or tarifa == "B":
        cuenta_mensual = cuenta_mensual - cuenta_mensual * 0.20
    else:
        cuenta_mensual = cuenta_mensual - cuenta_mensual * 0.14
elif consumo <= 499 and consumo >= 200:
    if tarifa == "A" or tarifa == "B":
        cuenta_mensual = cuenta_mensual - cuenta_mensual * 0.12
    else:
        cuenta_mensual = cuenta_mensual - cuenta_mensual * 0.08
if tarifa == "A" or tarifa == "B":
    cargo_de_medicion = cargo_de_medicion - cargo_de_medicion * 0.10
    if consumo >= 400:
        cargo_de_medicion = cargo_de_medicion - cargo_de_medicion * 0.05
print(cargo_de_medicion)
print(cuenta_mensual)

