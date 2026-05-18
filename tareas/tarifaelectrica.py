#Servicio de Energía Eléctrica
#Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio de medición.
#Valores base:
#Cuenta mensual: $45.000
#Cargo de medición: $6.000
#Reglas:
#Si el consumo es mayor o igual a 500 kWh:
#Tarifa A  → 20% descuento
#Tarifa B → 14% descuento
#Si el consumo está entre 200 y 499 kWh:
#Tarifa A o B → 12% descuento
#Tarifa C o D → 8% descuento
#Si el consumo es menor a 200 kWh → sin descuento.
#Cargo de medición:
#Tarifa A o B → 10% descuento.
#Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
descuento_medicion = 0
descuento = 0 
cuenta_mensual = 45000
cargo_medicion = 6000
consumo = float(input("Ingrese su consumo electrico :"))
tarifa = input("Ingrese la tarifa (A,B,C,D)").upper
if consumo >= 500:
    if tarifa == "A" or "B":
        cuenta_final = 0.20 # 20%
    else :
        cuenta_final = cuenta_mensual - (cuenta_mensual * 0.14) # 14%
elif 200 <= consumo <= 499:
    if tarifa == "A" or "B":
        descuento = 0.12 #12%
    else:
        descuento = 0.08 #8%
else :
    descuento = 0
print(cuenta_final)