#Variables base
plan_mensual = 28000
instalacion = 15000

#inputs 
print("------ Bienvenido a Telsur ------\n")
velocidad = int(input("Ingresa la velocidad del internet que deseas contratar (en Mbps): "))
print("\n¿Qué categría de plan deseas contratar")
print("- Categoría 1")
print("- Categoría 2")
print("- Categoría 3")
print("- Categoría 4")
categoria = int(input("Ingresa el número de la categoría seleccionada: "))

#Descuentos plan
if velocidad >= 600:
    if categoria == 1 or categoria == 2:
        plan_mensual -= (plan_mensual * 0.18)
    elif categoria == 3 or categoria == 4:
        plan_mensual -= (plan_mensual * 0.11)
elif 300 <= velocidad < 600:
    if categoria == 1 or categoria == 2:
        plan_mensual -= (plan_mensual * 0.1)
    elif categoria == 3 or categoria == 4:
        plan_mensual -= (plan_mensual * 0.06)
elif velocidad < 300:
    plan_mensual

#Descuentos instalación
if categoria == 1 or categoria == 2:
    instalacion -= (instalacion * 0.2)

if velocidad >= 500:
    instalacion -= (instalacion * 0.1)

print(f"Plan mensual: ${int(plan_mensual)}")
print(f"Instalación: ${int(instalacion)}")