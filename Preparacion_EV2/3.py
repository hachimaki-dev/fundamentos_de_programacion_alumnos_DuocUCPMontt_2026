#Desarrolle un programa que calcule el valor final de la mensualidad de un jardín infantil y el valor final del kit de materiales.
#Valores base:
#    Mensualidad: $85.000
#    Kit de materiales: $18.000
#Reglas de descuento para la mensualidad:
#    Edad <= 18 meses:
#        Nivel 1 o 2 → 20%
#        Nivel 3 o 4 → 13%
#    Edad entre 19 y 36 meses:
#        Nivel 1 o 2 → 12%
#        Nivel 3 o 4 → 7%
#    Edad > 36 meses → sin descuento.
#Reglas para el kit:
#    Nivel 1 o 2 → 10% descuento.
#    Si además la edad <= 12 meses → 5% adicional.
#Debe mostrar ambos valores finales.
mensualidad = 85000
kit = 18000
edad = int(input("ingrese la edad en meses:\n"))
nivel = input("ingrese el nivel de la clase:\n")
if edad <= 18:
    if nivel == "1" or nivel == "2":
        mensualidad -= mensualidad * 0.20
    else:
        mensualidad -= mensualidad * 0.13
if 19 <= edad <= 36:
    if nivel == "1" or nivel == "2":
        mensualidad -= mensualidad * 0.12
    else:
        mensualidad -= mensualidad * 0.07
if nivel == "1" or nivel == "2":
    kit -= kit * 0.10
    if edad <= 12:
        kit -= kit * 0.05
print(mensualidad)
print(kit)