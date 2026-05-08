cuenta = 45000
cargo_medicion = 6000

consumo = int(input("¿Cuántos kWh ha consumido?: "))

print("Seleccione su tarifa")
print("1. Tarifa A")
print("2. Tarifa B")
print("3. Tarifa C")
print("4. Tarifa D")
tarifa = int(input("¿Cuál es tu tarifa?: "))

descuento_cuenta = 0
descuento_medicion = 0

if consumo >= 500:
    if tarifa == 1 or tarifa == 2:
        descuento_cuenta = 0.20
    elif tarifa == 3 or tarifa == 4:
        descuento_cuenta = 0.14

if consumo >= 200 and consumo <= 499:
    if tarifa == 1 or tarifa == 2:
        descuento_cuenta = 0.12
    elif tarifa == 3 or tarifa == 4:
        descuento_cuenta = 0.08
    else:
        print("sin descuento")

if tarifa == 1 or tarifa == 2:
    descuento_medicion = 0.10
    if consumo >= 400:
        descuento_medicion += 0.05


cuenta_final = cuenta - (cuenta * descuento_cuenta)
medicion_final = cargo_medicion - (cargo_medicion * descuento_medicion)

print(f"Cuenta final: ${cuenta_final}")
print(f"cargo de medicion final: ${medicion_final}")