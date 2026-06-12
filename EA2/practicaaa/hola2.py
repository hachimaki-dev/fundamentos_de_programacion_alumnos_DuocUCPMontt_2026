mensualidad = 85000
kit = 18000

print("---BIENVENIDO A LA SALA CUNA---\n  Recordar que solo nenes de \n     3 a 48 meses son\n  aceptados en el recinto...")
edad = int(input("¿cuantos meses tien su hijito?:"))
curso = int(input("¿en que curso va a ir su hijo (1,2,3,4)?:"))

descuento = 0

if edad <= 18:
    if curso == 1 or curso == 2:
        descuento = 0.20
    elif curso == 3 or curso == 4:
        descuento = 0.13
    else:
        descuento = 0
elif 19 <= edad <= 36:
    if curso == 1 or curso == 2:
        descuento = 0.12
    elif curso == 3 or curso == 4:
        descuento = 0.07
    else:
        descuento = 0
else:
    edad > 36 
    descuento = 0

descuento_mensual = mensualidad * descuento
cuota_mensual = mensualidad - descuento_mensual

descuento_kit = 0
if curso == 1 or curso == 2:
    descuento_kit += 0.10
if edad <= 12:
    descuento_kit += 0.05

kit_descuento = kit * descuento_kit
valor_kit = kit - kit_descuento

print(f"total de la cuota mensual de la sala cuna es ${int(cuota_mensual)}")
print(f"total del kit es ${int(valor_kit)}")
