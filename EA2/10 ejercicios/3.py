'''Ejercicio 3: Jardín Infantil
MEDIUM
Desarrolle un programa que calcule el valor final de la mensualidad de un jardín infantil y el valor final del kit de materiales.

Valores base:

Mensualidad: $85.000
Kit de materiales: $18.000
Reglas de descuento para la mensualidad:

Edad <= 18 meses:
Nivel 1 o 2 → 20%
Nivel 3 o 4 → 13%
Edad entre 19 y 36 meses:
Nivel 1 o 2 → 12%
Nivel 3 o 4 → 7%
Edad > 36 meses → sin descuento.
Reglas para el kit:

Nivel 1 o 2 → 10% descuento.
Si además la edad <= 12 meses → 5% adicional.
Debe mostrar ambos valores finales.'''

mensualidad = 85000
materiales = 18000
edad = int(input("ingrese la edad en meses: "))
nivel = int(input("ingrese el nivel: "))

if edad <= 18:
    if nivel == 1 or 2:
        descuento_mensual = mensualidad * 0.2
        mensualidad -= descuento_mensual
    else:
        descuento_mensual = mensualidad * 0.13
        mensualidad -= descuento_mensual
elif 19 >= edad <= 36:
    if nivel == 1 or 2:
        descuento_mensual = mensualidad * 0.12
        mensualidad -= descuento_mensual
    else:
        descuento_mensual = mensualidad * 0.07
        mensualidad -= descuento_mensual

if nivel == 1 or 2:
    descuento_materiales = materiales * 0.1
    materiales -= descuento_materiales
    if edad <= 12:
        descuento_materiales = materiales * 0.05
        materiales -= descuento_materiales

print(f"Mensualidad: {int(mensualidad)}")
print(f"Kit materiales: {int(materiales)}")