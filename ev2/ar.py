#Desarrolle un programa en Python que calcule el valor final de la cuenta mensual de energía eléctrica y el valor final del cargo por servicio de medición.

#Valores base:

#Cuenta mensual: $45.000
#Cargo de medición: $6.000
#Reglas de descuento para la cuenta:

#Si el consumo es mayor o igual a 500 kWh:
#Tarifa A o B → 20% descuento
#Tarifa C o D → 14% descuento
#Si el consumo está entre 200 y 499 kWh:
#Tarifa A o B → 12% descuento
#Tarifa C o D → 8% descuento
#Si el consumo es menor a 200 kWh → sin descuento.
#Reglas para el cargo de medición:

#Tarifa A o B → 10% descuento.
#Si además el consumo es mayor o igual a 400 kWh → 5% adicional.
#Debe mostrar ambos valores finales.
 
cuenta_mensual = 45000
cargo_medicion = 6000

consumo = int(input())


tarifa = input()

if consumo >= 500: 
    if tarifa in ["A","B"]:
        descuento_cuenta = 0.20
    else:
        descuento_cuenta = 0.14
        
elif consumo >= 200: 
    if tarifa in ["C","D"]:
        descuento_cuenta = 0.12
    else:
        descuento_cuenta = 0.08
    
    
else:
    descuento_cuenta = 0
    
valor_final_cuenta = cuenta_mensual - (cuenta_mensual * descuento_cuenta)

if tarifa in ["A","B"]:
    descuento_medicion = 0.10
    if consumo >= 400:
        descuento_cuenta = 0.05
    else:
        descuento_medicion = 0
        
valor_final_medicion =cargo_medicion - (cargo_medicion * descuento_medicion)

print(valor_final_cuenta)
print(valor_final_medicion)
    


    
    
        