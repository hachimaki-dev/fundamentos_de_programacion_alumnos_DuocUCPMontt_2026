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
    if tarifa in ["A","B"]:
        descuento_cuenta = 0.12
    else:
        descuento_cuenta = 0.08
    
else:
    descuento_cuenta = 0
    
valor_final_cuenta = cuenta_mensual * (1 - descuento_cuenta)

if tarifa in ["A","B"]:
    descuento_medicion = 0.10
    if consumo >= 400:
        descuento_medicion = 0.15
else:
    descuento_medicion = 0
        
valor_final_medicion = cargo_medicion * (1 - descuento_medicion)

print(valor_final_cuenta)
print(valor_final_medicion)