# Ejercicio 1: Servicio de Energía Eléctrica
# MEDIUM

# valor base

cuenta_mensual = 45000
cargo_medicion = 6000
consumo = int(input('Ingrese el consumo en kWh: '))
tarifa = input('Ingrese la tarifa (A, B, C o D): ').upper()

if consumo >= 500:
    
    if tarifa == 'A' or tarifa == 'B':
        
        descuento_cuenta = 20

    elif tarifa == 'C' or tarifa == 'D':

        descuento_cuenta = 14  

elif consumo >= 200 and consumo <= 499:

    if tarifa == 'A' or tarifa == 'B':
        
        descuento_cuenta = 12

    elif tarifa == 'C' or tarifa == 'D':
        
        descuento_cuenta = 8
else:
    descuento_cuenta = 0

# Calcular descuento cuenta mensual

monto_descuento_cuenta = cuenta_mensual * descuento_cuenta / 100
valor_final_cuenta = cuenta_mensual - monto_descuento_cuenta

    # DESCUENTO CARGO MEDICIÓN

valor_final_medicion = cargo_medicion

if tarifa == 'A' or tarifa == 'B':
    
    # Primer descuento 10%
    valor_final_medicion = valor_final_medicion * 0.90
    
    # Descuento adicional 5%

    if consumo >= 400:
         valor_final_medicion = valor_final_medicion * 0.95

# Calcular descuento medición


print('Valor final cuenta mensual: $', int(valor_final_cuenta))
print('Valor final cargo medición: $', int(valor_final_medicion))

