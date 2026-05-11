plan_mensual = 28000
instalacion = 15000

velocidad = int(input("¿Cuantos Mbps desea contratar?: "))
categoria = int(input("¿Que categoria desea instalar? (1-2-3-4): "))

if velocidad >= 600:
    if categoria == 1 or categoria == 2:
        descuento_plan_mensual = 0.18
    else:
        descuento_plan_mensual = 0.11

elif 300 <= velocidad < 600:
    if categoria == 1 or categoria == 2:
        descuento_plan_mensual = 0.10
    else:
        descuento_plan_mensual = 0.06

else:
    descuento_plan_mensual = 0

descuento_instalacion = 0
if categoria == 1 or categoria == 2:
    descuento_instalacion = 0.20
    if velocidad >= 500:
        descuento_instalacion += 0.10

valor_final_plan_mensual = plan_mensual * (1 - descuento_plan_mensual)
valor_final_instalacion = instalacion * (1 - descuento_instalacion)

print(f"El valor final del plan mensual es de: ${valor_final_plan_mensual}")
print(f"El valor final de la instalacion es de: ${valor_final_instalacion}")
