prima_mensual = 22000
chip = 9000

peso = int(input())
cobertura = (input())

if peso >= 20:
    if cobertura in ["A","B"]:
        descuento = 0.16
    else:
        descuento = 0.10
elif 8 <= peso < 20:
    if cobertura in ["A","B"]:
        descuento = 0.10
    else:
        descuento = 0.06
else:
    descuento = 0
    
prima_mensual = prima_mensual * (1 - descuento)

if cobertura in ["A","B"]:
    chip = chip * (1 - 0.12)
    if peso >= 15:
        chip = chip * (1 - 0.06)
else:
    chip = chip
    

print(prima_mensual)
print(chip)