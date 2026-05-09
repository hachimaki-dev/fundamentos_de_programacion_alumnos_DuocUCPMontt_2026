Mensualidad = 85000
Kit_de_materiales = 18000

meses = int(input("cuantos meses tiene su niño/a:"))

print("seleccione en el nivel que va su niño/a")
print("1. nivel 1")
print("2. nivel 2")
print("3. nivel 3")
print("4. nivel 4")

nivel = int(input("ingrese el numero segun el nivel:"))

if meses <= 18:
    if nivel == 1 or nivel == 2:
        Mensualidad = Mensualidad * (1 - 0.20)
    elif nivel == 3 or nivel == 4:
       Mensualidad = Mensualidad * (1 - 0.13)

if meses >= 19 and meses <= 36:
    if nivel == 1 or nivel == 2:
        Mensualidad = Mensualidad * (1 - 0.12)
    elif nivel == 3 or nivel == 4:
        Mensualidad = Mensualidad * (1 - 0.07)
    else:
        print("sin descuento")

if nivel == 1 or nivel == 2:
    Kit_de_materiales = Kit_de_materiales * 0.90
if meses <= 12:
    Kit_de_materiales = Kit_de_materiales * 0.95

print(f"el total de la mensualidad es de: ${Mensualidad}")
print(f"el total del kit de materiales es de: ${Kit_de_materiales}")
