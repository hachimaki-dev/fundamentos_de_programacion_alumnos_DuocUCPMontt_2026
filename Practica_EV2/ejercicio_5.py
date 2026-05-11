prima_mensual = 22000
chip = 9000

peso = int(input("Ingrese el peso de su mascota (KG): "))
cobertura = input("¿Que tipo de cobertura desea comprar? (A, B, C, D): ").upper()

if peso >= 20:
    if cobertura == "A" or cobertura == "B":
        descuento_prima_mensual = 0.16
    else:
        descuento_prima_mensual = 0.10

elif 8 <= peso < 20:
    if cobertura == "A" or cobertura == "B":
        descuento_prima_mensual = 0.10
    else:
        descuento_prima_mensual = 0.06

else:
    descuento_prima_mensual = 0

descuento_chip = 0
if cobertura == "A" or cobertura == "B":
    descuento_chip = 0.12
    if peso >= 15:
        descuento_chip += 0.06

valor_final_prima_mensual = prima_mensual * (1 - descuento_prima_mensual)
valor_final_chip = chip * (1 - descuento_chip)

print(f"El valor final de la prima mensual es de: ${int(valor_final_prima_mensual)}")
print(f"El valor final del chip es de: ${int(valor_final_chip)}")