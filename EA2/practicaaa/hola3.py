plan_mensual = 28000
instalacion = 15000

print("===Tu fibra optica===")
velocidad = int(input("cuantos Mgps requiere (600 o +, 300 o 599 o - 300):"))
categoria = int(input("que categoria va a seleciona (1,2,3,4,):"))

descuento = 0

if velocidad >= 600:
    if categoria == 1 or categoria == 2:
        descuento = 0.18
    elif categoria == 3 or categoria == 4:
        descuento = 0.11
    else:
        descuento = 0
elif 300 <= velocidad < 600:
    if categoria == 1 or categoria == 2:
        descuento = 0.10
    elif categoria == 3 or categoria == 4:
        descuento = 0.06
    else:
        descuento = 0
else:
    descuento = 0

descuento_mensual = plan_mensual * descuento
cuota_mensual = plan_mensual - descuento_mensual

print (int(cuota_mensual))

