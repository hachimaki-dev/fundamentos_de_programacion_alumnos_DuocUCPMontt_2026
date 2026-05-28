precio_por_noche = 15000
seguro = 5000

dias = int(input("Ingresa los dias: "))
tramo = input("ingrese su tramo (A, B, C, D): ").upper()

valor_camping_bruto = precio_por_noche * dias
descuento_camping = 0.0

if dias <= 5:
    if tramo == "A" or tramo == "B":
        descuento_camping = 0.10
    elif tramo == "C" or tramo == "D":
        descuento_camping = 0.05

elif 6 <= dias <= 12:
    if tramo == "A" or tramo == "B":
        descuento_camping = 0.20
    elif tramo == "C" or tramo == "D":
        descuento_camping = 0.15
else:
    descuento_camping = 0.0

descuento_seguro = 0.0

if tramo == "A" or tramo == "B":
    descuento_seguro = descuento_seguro + 0.15
    if dias >= 10:
        descuento_seguro = descuento_seguro + 0.05

    valor_camping_final = valor_camping_bruto * (1- descuento_camping)
    valor_seguro_final = seguro * (1- descuento_seguro)

print(f"El valor del camping: {int(valor_camping_final)}")
print(f"El valor del seguro: {int(valor_seguro_final)}")