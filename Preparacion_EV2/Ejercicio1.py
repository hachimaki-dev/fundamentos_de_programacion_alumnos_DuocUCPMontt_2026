cuenta_mensual = 45000
cargo_de_medicion = 6000
consumo_kWh = int(input("¿Cuantos kWh ha consumido este mes? "))
tipo_tarifa = (input("¿Que tipo de tarifa tiene asignada? "))

if consumo_kWh >= 500:
    if tipo_tarifa == "A" or tipo_tarifa == "B":
        cuenta_mensual = cuenta_mensual * 0.80
    elif tipo_tarifa == "C" or tipo_tarifa == "D":
        cuenta_mensual = cuenta_mensual * 0.86
elif consumo_kWh <= 499 and consumo_kWh >= 200:
    if tipo_tarifa == "A" or tipo_tarifa == "B":
        cuenta_mensual = cuenta_mensual * 0.88
    elif tipo_tarifa == "C" or tipo_tarifa == "D":
        cuenta_mensual = cuenta_mensual * 0.92
elif consumo_kWh < 200:
    print("Sin descuento")

if tipo_tarifa == "A" or tipo_tarifa == "B":
    cargo_de_medicion = cargo_de_medicion * 0.90
if consumo_kWh >= 400:
    cargo_de_medicion = cargo_de_medicion * 0.95

print(f"Cuenta energía: {cuenta_mensual} \nCargo medicion: {cargo_de_medicion}")