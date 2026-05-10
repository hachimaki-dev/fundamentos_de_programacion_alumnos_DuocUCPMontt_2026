'''Desarrolle un programa que calcule el valor final de un plan de internet y el valor final del cargo de instalación.

Valores base:

    Plan mensual: $28.000
    Instalación: $15.000

Reglas de descuento del plan:

    Velocidad >= 600 Mbps:
        Categoría 1 o 2 → 18%
        Categoría 3 o 4 → 11%
    300 <= velocidad < 600 Mbps:
        Categoría 1 o 2 → 10%
        Categoría 3 o 4 → 6%
    Menor a 300 Mbps → sin descuento.

Reglas instalación:

    Categoría 1 o 2 → 20% descuento.
    Si además la velocidad >= 500 Mbps → 10% adicional.

Debe mostrar ambos valores finales.'''

plan = 28000
instalacion = 15000
velocidad = int(input("Ingrese la velocidad en mbps: "))
categoria = int(input("Ingrese su categoria(1-2-3-4): "))
descuento_plan = 0
descuento_instalacion = 0

if velocidad >= 600:
    if categoria == 1 or 2:
        descuento_plan = plan * 0.18
        plan -= descuento_plan
    else:
        descuento_plan = plan * 0.11
        plan -= descuento_plan
elif 300 <= velocidad < 600:
    if categoria == 1 or 2:
        descuento_plan = plan * 0.1
        plan -= descuento_plan
    else:
        descuento_plan = plan * 0.06
        plan -= descuento_plan

if categoria == 1 or 2:
    descuento_instalacion = instalacion * 0.2
    instalacion -= descuento_instalacion
    if velocidad >= 500:
        descuento_instalacion = instalacion * 0.1
        instalacion -= descuento_instalacion
        
print(f"Plan mensual: {int(plan)}")
print(f"Instalacion: {int(instalacion)}")