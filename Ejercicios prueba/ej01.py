cuenta_mensual = 45000
medicion = 6000

consumo_kWh = int(input("Ingrese su consumo (kWh): "))
tarifa = input("Ingrese su tipo de tarifa (use letras mayúsculas): ").upper()

#Descuento para la cuenta
if consumo_kWh >= 500:
    if tarifa == 'A' or tarifa == 'B':
        cuenta_mensual = cuenta_mensual - (cuenta_mensual * 0.2)
    elif tarifa == 'C' or tarifa == 'D':
        cuenta_mensual = cuenta_mensual - (cuenta_mensual * 0.14)
elif consumo_kWh >= 200 and consumo_kWh <= 499:
    if tarifa == 'A' or tarifa == 'B':
        cuenta_mensual = cuenta_mensual - (cuenta_mensual * 0.12)
    elif tarifa == 'C' or tarifa == 'D':
        cuenta_mensual = cuenta_mensual - (cuenta_mensual * 0.08)
elif consumo_kWh < 200:
    cuenta_mensual

#Descuento para la medición
if tarifa == 'A' or tarifa == 'B':
    medicion = medicion - (medicion * 0.1)

if consumo_kWh >= 400:
    medicion = medicion - (medicion * 0.05)

print(f"Total a pagar: ${int(medicion + cuenta_mensual)}")
print(f"Cuenta energía: $ {int(cuenta_mensual)}")
print(f"Cargo medición: ${int(medicion)}")