plan_mensual = 28000
instalacion = 15000

velocidad = int(input("cuales su velocidad de internet?:"))
          
print("indique cual es su categorias porfavor:")
print("1. categoria 1")
print("2. categoria 2")
print("3. categoria 3")
print("4. categoria 4")

categoria = int(input("eliga una opcion porfavor:"))

if velocidad >= 600:
    if categoria == 1 or categoria == 2:
        plan_mensual = plan_mensual * (1 - 0.18)
    elif categoria == 3 or categoria == 4:
        plan_mensual = plan_mensual * (1 - 0.11)

if velocidad >= 300 and velocidad <= 599:
    if categoria == 1 or categoria == 2:
        plan_mensual = plan_mensual * (1 - 0.10)
    elif categoria == 3 or categoria == 4:
        plan_mensual = plan_mensual * (1 - 0.06)
    else:
        print("sin descuento")

if categoria == 1 or categoria == 2:
    instalacion = instalacion * 0.80

if velocidad >= 500:
    instalacion = instalacion * 0.90

print(f"el total del plan mensual es de: ${plan_mensual}")
print(f"el total de su instalacion es de: ${instalacion}")