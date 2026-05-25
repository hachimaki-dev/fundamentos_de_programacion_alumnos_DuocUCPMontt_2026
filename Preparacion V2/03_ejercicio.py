# Ejercicio 3: Jardín Infantil
# Desarrolle un programa que calcule el valor final de la mensualidad
#  de un jardín infantil y el valor final del kit de materiales.

 # valores base:

mensualidad = 85000
kit_materiales = 18000
edad = int(input('Ingrese la edad en meses: '))
nivel = int(input('Ingresa el nivel (1, 2, 3, 4): '))

# calculadora de la mensualidad

if edad <= 18 :

    if nivel == 1 or nivel == 2:

        descuento_nivel = 20

    elif nivel == 3 or nivel == 4:

        descuento_nivel = 13

elif edad >= 19 and edad <= 36:

    if nivel == 1 or nivel == 2:

        descuento_nivel = 12

    elif nivel == 3 or nivel == 4:

        descuento_nivel = 7

else:
    descuento_nivel = 0

monto_descuento_mensualidad = mensualidad * descuento_nivel / 100
valor_final_menbresia = mensualidad - monto_descuento_mensualidad

# calculadora del kit de materiales

valor_final_kit_materiales = kit_materiales

if nivel == 1 or nivel == 2:

    # primer descuento 10%
    valor_final_kit_materiales = valor_final_kit_materiales * 0.90

    if edad <= 12:

        # segundo descuento 5%
        valor_final_kit_materiales = valor_final_kit_materiales * 0.95

print('valor final de la mensualidad: $',int(valor_final_menbresia))
print('valor fianl del kit de materiales: $', int(valor_final_kit_materiales))

