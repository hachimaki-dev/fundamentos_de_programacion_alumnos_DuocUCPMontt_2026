cuota_mensual = 45000
cargo_de_mediacion = 6000

consumo = int(input("ingrese su consumo en kWh:"))
tarifa = input("tarifa: (a,b,c,d):")

if consumo <= 500:
    if tarifa == 'a' or tarifa == 'b':
        descuento = 20
    elif tarifa == 'c' or tarifa == 'd':
        descuento = 14
    else:
        descuento = 0
elif consumo >=200 and consumo <=499:
    if tarifa == 'a' or tarifa == 'b':
        descuento = 12
    elif tarifa == 'c' or tarifa == 'd':
        descuento = 8
    else:
       descuento = 0
else:
    descuento = 0

valor_descuento = cuota_mensual * descuento / 100
cuota_final = cuota_mensual - valor_descuento

descuento_mediacion = 0

if tarifa == 'a' or tarifa == 'b':
    descuento = 10
    if consumo >= 400:
        descuento_mediacion += 5

valor_descuento_mediacion = cargo_de_mediacion * descuento_mediacion / 100
mediacion_final = cargo_de_mediacion - valor_descuento_mediacion

print("cuota final:", cuota_final)
print("mediacion final", mediacion_final)