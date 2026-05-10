'''Desarrolle un programa que calcule el valor final de la prima mensual de un seguro de mascota y el valor final del chip de identificación.

Valores base:

    Prima mensual: $22.000
    Chip: $9.000

Reglas de descuento de la prima:

    Peso >= 20 kg:
        Cobertura A o B → 16%
        Cobertura C o D → 10%
    8 <= peso < 20 kg:
        Cobertura A o B → 10%
        Cobertura C o D → 6%
    Menor a 8 kg → sin descuento.

Reglas del chip:

    Cobertura A o B → 12% descuento.
    Si además el peso >= 15 kg → 6% adicional.

Debe mostrar ambos valores finales.'''

prima = 22000
chip = 9000
peso = int(input("Ingrese el peso de su mascota en kg: "))
cobertura = input("Ingrese su tipo de cobertura(A-B-C-D): ").upper()
descuento_prima = 0
descuento_chip = 0

if peso >= 20:
    if cobertura == 'A' or 'B':
        descuento_prima = prima * 0.16
        prima -= descuento_prima
    else:
        descuento_prima = prima * 0.1
        prima -= descuento_prima
elif 8 <= peso < 20:
    if cobertura == 'A' or 'B':
        descuento_prima = prima * 0.1
        prima -= descuento_prima
    else:
        descuento_prima = prima * 0.06
        prima -= descuento_prima

if cobertura == 'A' or 'B':
    descuento_chip = chip * 0.12
    chip -= descuento_chip
    if peso >= 15:
        descuento_chip = chip * 0.06
        chip -= descuento_chip
        
print(f"Prima mensual: {int(prima)}")
print(f"Chip: {int(chip)}")