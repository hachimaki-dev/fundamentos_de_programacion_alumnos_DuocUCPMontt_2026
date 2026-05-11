cuenta_mensual = 45000
cargo_de_medicion = 6000
consumo = int(input("Ingrese su consumo (kWh): "))
tarifa = input("Seleccion su tarifa (A, B, C , D): ").upper()

if consumo >= 500:
    if tarifa == "A" or tarifa == "B":
        descuento = 0.20
    else:
        descuento = 0.14

elif consumo >= 200:
    if tarifa == "A" or tarifa == "B":
        descuento = 0.12
    else:
        descuento = 0.08
else:
    descuento = 0

descuento_medicion = 0

if tarifa == "A" or tarifa == "B":
    descuento_medicion = 0.10
    if consumo >= 400:
        descuento_medicion += 0.05

valor_final_cuenta = cuenta_mensual * (1 - descuento)
valor_final_medicion = cargo_de_medicion * (1 - descuento_medicion)

print(f"Valor final de la cuenta mensual es de: ${valor_final_cuenta}")
print(f"Valor final del cargo por servicio de medicion es de: ${valor_final_medicion}")
