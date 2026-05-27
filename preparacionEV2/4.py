#Desarrolle un programa que calcule el valor final de un plan de internet y el valor final del cargo de instalación.

#Valores base:

#Plan mensual: $28.000
#Instalación: $15.000
#Reglas de descuento del plan:

#Velocidad >= 600 Mbps:
#Categoría 1 o 2 → 18%
#Categoría 3 o 4 → 11%
#300 <= velocidad < 600 Mbps:
#Categoría 1 o 2 → 10%
#Categoría 3 o 4 → 6%
#Menor a 300 Mbps → sin descuento.
#Reglas instalación:

#Categoría 1 o 2 → 20% descuento.
#Si además la velocidad >= 500 Mbps → 10% adicional.
#Debe mostrar ambos valores finales.
plan_mensuales = 28000
instalacion = 15000
velocidad = int(input("ingrese velocidad de internet"))
categoria = int(input("ingrese la categoria(1,2,3,4)"))
if velocidad >= 600:
    if categoria == 1 or categoria ==2:
        plan_mensuales *= 0.82
    elif categoria == 3 or categoria == 4:
        plan_mensuales *= 0.89
elif 300 <= velocidad < 600:
    if categoria == 1 or categoria == 2:
        plan_mensuales *= 0.90
    elif categoria == 3 or categoria == 4:
        plan_mensuales *= 0.94
elif velocidad < 300:
    print("sin descuento")
if categoria == 1 or categoria == 2:
    instalacion *= 0.80
    if velocidad >= 500:
        instalacion *= 0.90
print(f"plan mensual es: {plan_mensuales} \n la instalacion es: {instalacion}")
