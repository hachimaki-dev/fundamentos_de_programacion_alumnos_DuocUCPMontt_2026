mensualidad = 85000
kit = 18000

edad = int(input("Ingrese la edad de su hijo/a en meses: "))
nivel = int(input("¿Que nivel de kit va a comprar? (1-2-3-4): "))

if edad <= 18:
    if nivel == 1 or nivel == 2:
        descuento_mensualidad = 0.20
    else:
        descuento_mensualidad = 0.13

elif 19 <= edad < 36:
    if nivel == 1 or nivel == 2:
        descuento_mensualidad = 0.12
    else:
        descuento_mensualidad = 0.07

else:
    descuento_mensualidad = 0

descuento_kit = 0
if nivel == 1 or nivel == 2:
    descuento_kit == 0.10
    if edad <= 12:
        descuento_kit += 0.05

valor_final_mensualidad = mensualidad * (1 - descuento_mensualidad)
valor_final_kit = kit * (1 - descuento_kit)

print(f"El valor final de la mensualidad es de: ${valor_final_mensualidad}")
print(f"El valor final del kit de materiales es de: ${valor_final_kit}")