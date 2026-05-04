curanto = 7500
carbonada = 2200
onigiri = 2500
bush_tucker = 38000
fårikål = 53000
arroz_jollof = 47500

print("curanto: $7500")
print("carbonada: $2200")
print("onigiri: $2500")
print("bush tucker: $38000")
print("fårikål: $53000")
print("arroz jollof: $47500")
print()

contador = int(input("¿cuántos platos desea pedir? "))
subtotal = 0

while contador > 0 :
    print("ingrese comida del menú: ")
    comida = input()
    if "curanto" == comida :
        subtotal += 7500
        contador -= 1
    elif "carbonada" == comida :
        subtotal += 2200
        contador -= 1
    elif "onigiri" == comida :
        subtotal += 2500
        contador -= 1
    elif "bush tucker" == comida :
        subtotal += 38000
        contador -= 1
    elif "fårikål" == comida :
        subtotal += 53000
        contador -= 1
    elif "arroz jallof" == comida :
        subtotal += 47500
        contador -= 1
if subtotal < 15000 :
    print(f"subtotal: ${subtotal}")
    subtotal += 2000
    print("costo de envío: $2000")
    print(f"total: ${subtotal}")
elif subtotal >= 15000 :
    print(f"subtotal: ${subtotal}")
    print("descuento: 10%")
    subtotal *= 0.9
    print(f"total: ${subtotal}")