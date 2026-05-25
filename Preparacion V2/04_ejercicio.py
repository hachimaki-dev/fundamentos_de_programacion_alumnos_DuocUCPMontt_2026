# Ejercicio 4: Fibra Óptica
# Desarrolle un programa que calcule el valor final de un plan de internet y
#  el valor final del cargo de instalación.

# Valores base

plan_mensual = 28000
instalacion = 15000
velosidad = int(input('Ingresa la velocidad: '))
categoria = int(input('Ingresa la categoria (1, 2, 3, 4): '))

# calculadora de descuento del plan mensual

if velosidad >= 600:

    if categoria == 1 or categoria == 2:

        descuento_categoria = 18

    elif categoria == 3 or categoria == 4:
    
        descuento_categoria = 11

elif velosidad >= 300 and velosidad <= 600:

    if categoria == 1 or categoria == 2:
        
        descuento_categoria = 10

    elif categoria == 3 or categoria == 4:

        descuento_categoria = 6

else:
    descuento_categoria = 0

monto_plan_mensual = plan_mensual * descuento_categoria / 100
valor_final_plan_mensual = plan_mensual - monto_plan_mensual 

# calculadora de instalacion
valor_final_instalacion = instalacion

if categoria == 1 or categoria == 2:

    # primer descuento 20%
    valor_final_instalacion = valor_final_instalacion * 0.80

    if velosidad >= 500:

        # segundo descuento 10%
        valor_final_instalacion = valor_final_instalacion * 0.90

print('valor final del plan mensual: $', int(valor_final_plan_mensual))
print('valor final de instalacion: %', int(valor_final_instalacion))
