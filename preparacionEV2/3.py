#Desarrolle un programa que calcule el valor final de la mensualidad de un jardín infantil y el valor final del kit de materiales.

#Valores base:

#Mensualidad: $85.000
#Kit de materiales: $18.000
#Reglas de descuento para la mensualidad:

#Edad <= 18 meses:
#Nivel 1 o 2 → 20%
#Nivel 3 o 4 → 13%
#Edad entre 19 y 36 meses:
#Nivel 1 o 2 → 12%
#Nivel 3 o 4 → 7%
#Edad > 36 meses → sin descuento.
#Reglas para el kit:

#Nivel 1 o 2 → 10% descuento.
#Si además la edad <= 12 meses → 5% adicional.
#Debe mostrar ambos valores finales.
mensualidad = 85000
kit_de_materiales = 18000
edad = int(input("ingrese la edad"))
nivel = int(input("ingrese nivel 1 , 2, 3, 4"))
if edad <= 18:
    if nivel == 1 or nivel == 2:
        mensualidad *= 0.80
    elif nivel == 3 or nivel == 4:
        mensualidad *= 0.87
elif edad > 19 < 36:
    if nivel == 1 or nivel == 2:
        mensualidad *= 0.88
    elif nivel == 3 or nivel == 4:
        mensualidad *= 0.93
elif edad > 36:
    print("sin descuento")
if nivel == 1 or nivel == 2:
    kit_de_materiales *= 0.90
    if edad <= 12:
        kit_de_materiales *= 0.95
print(f"mensualidad:{mensualidad} \n kit de materiales: {kit_de_materiales}")

