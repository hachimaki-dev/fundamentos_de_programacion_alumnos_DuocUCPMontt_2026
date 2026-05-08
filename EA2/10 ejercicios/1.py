'''Ejercicio 1: Servicio de Energía Eléctrica
MEDIUM
Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio de medición.

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
Debe mostrar ambos valores finales.'''


int(cuenta_mensual) = 45000
medicion = 6000
consumo = int(input("Ingrese el consumo: "))
tarifa = str(input("Ingrese su tarifa (A-B-C-D): ")).upper
descuento_cuenta = 0
descuento_medicion = 0

if consumo >= 500:
    if tarifa == 'A' or 'B':
        descuento_cuenta = cuenta_mensual * 0.2
        cuenta_mensual -= descuento_cuenta
    else:
        descuento_cuenta = cuenta_mensual * 0.14
        cuenta_mensual -= descuento_cuenta
elif consumo <= 499 and consumo >= 200:
    if tarifa == 'A' or 'B':
        descuento_cuenta = cuenta_mensual * 0.12
        cuenta_mensual -= descuento_cuenta
    else:
        descuento_cuenta = cuenta_mensual * 0.08
        cuenta_mensual -= descuento_cuenta
if tarifa == 'A' or 'B':
    descuento_medicion = medicion * 0.1
    medicion -= descuento_medicion
    if consumo >= 400:
        descuento_medicion = medicion * 0.5
        cuenta_mensual -= descuento_medicion

print(cuenta_mensual)
print(medicion)