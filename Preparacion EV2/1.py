cuenta_mensual = 45000
carga_medicion = 6000

cuenta_energia_total = 0
cargo_medicion_total = 0

consumo = -1

while consumo < 0:
    consumo = int(input("\nConsumo (kWh): "))

    if consumo < 0:
        print("El consumo no puede ser menor a 0")

tarifa = ""

if tarifa not in ["A", "B", "C", "D"]:
    tarifa = input("\nTarfia: ").upper()

    if tarifa not in ["A", "B", "C", "D"]:
        print("Ingrese una tarifa válida")

if consumo >= 500:
    if tarifa == "A" or tarifa == "B":
        descuento_consumo = .20
    else:
        descuento_consumo = .14
elif consumo >= 200 and consumo <= 499:
    if tarifa == "A" or tarifa == "B":
        descuento_consumo = .12
    else:
        descuento_consumo = .08
else:
    descuento_consumo = 0

if tarifa == "A" or tarifa == "B":
    descuento_cargo = .1

    if consumo >= 400:
        descuento_cargo_adicional = .05
    else:
        descuento_cargo_adicional = 0
else:
    descuento_cargo = 0
    descuento_cargo_adicional = 0

cuenta_energia_total = int(cuenta_mensual * (1 - descuento_consumo))
cargo_medicion_total = int((carga_medicion * (1 - descuento_cargo)) * (1 - descuento_cargo_adicional))

print(f"Cuenta energía: {cuenta_energia_total}")
print(f"Cargo medición: {cargo_medicion_total}")