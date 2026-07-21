# Desarrolle un programa que calcule el valor final de un plan de internet y el valor final del cargo de instalación.

# Valores base:

# Plan mensual: $28.000
# Instalación: $15.000
# Reglas de descuento del plan:

# Velocidad >= 600 Mbps:
# Categoría 1 o 2 → 18%
# Categoría 3 o 4 → 11%
# 300 <= velocidad < 600 Mbps:
# Categoría 1 o 2 → 10%
# Categoría 3 o 4 → 6%
# Menor a 300 Mbps → sin descuento.
# Reglas instalación:

# Categoría 1 o 2 → 20% descuento.
# Si además la velocidad >= 500 Mbps → 10% adicional.
# Debe mostrar ambos valores finales.

# Input Esperado
# 700
# 1

# Output Esperado
# Plan mensual: 22960
# Instalacion: 10800

velocidad = int(input("¿Cúal es la velocidad de internet?: "))
categoria = int(input("¿Cúal es la categoria de intenet?: "))

plan_mensual = 28000
instalacion = 15000

if velocidad >= 600:
    if categoria in [1, 2]:
        plan_mensual *= 0.82
    elif categoria in [3, 4]:
        plan_mensual *= 0.89
elif 300 <= velocidad < 600:
    if categoria in [1 , 2]:
        plan_mensual *= 0.90
    elif categoria in [3, 4]:
        plan_mensual *= 0.94
elif velocidad < 300:
    plan_mensual *= 100
else: 
    print("Ingrese un número valido")

#categoria

if categoria in [1, 2]:
    instalacion *= 0.80
    if velocidad >= 500:
        instalacion *= 0.90

print(f"Plan Mensual: {int(plan_mensual)}")
print(f"Instalación: {int(instalacion)}")