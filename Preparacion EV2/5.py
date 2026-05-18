mensualidad = 22000
chip = 9000

peso = 0

while peso < 1:
    peso = int(input("Peso (Kg): "))

    if peso < 1:
        print("Ingrese un peso válido")

cobertura = ""

while cobertura not in ["A", "B", "C", "D"]:
    cobertura = input("Cobertura: ").upper()

    if cobertura not in ["A", "B", "C", "D"]:
        print("Ingrese una cobertura válida")

if peso >= 20:
    if cobertura == "A" or cobertura == "B":
        dcto_mensualidad = .16
    else:
        dcto_mensualidad = .1
elif peso >= 8 and peso < 20:
    if cobertura == "A" or cobertura == "B":
        dcto_mensualidad = .1
    else:
        dcto_mensualidad = .06
else:
    dcto_mensualidad = 0

if cobertura == "A" or cobertura == "B":
    dcto_chip = .12

    if peso >= 15:
        dcto_chip_adicional = .06
    else:
        dcto_chip_adicional = 0
else:
    dcto_chip = 0
    dcto_chip_adicional = 0

mensualidad_final = int(mensualidad * (1 - dcto_mensualidad))
chip_final = int((chip * (1 - dcto_chip)) * (1 - dcto_chip_adicional))

print(f"Prima mensual: {mensualidad_final}")
print(f"Chip: {chip_final}")