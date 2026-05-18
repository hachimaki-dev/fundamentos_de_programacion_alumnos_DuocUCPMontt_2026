# Ejercicio 5: Seguro de Mascota
# MEDIUM
# Desarrolle un programa que calcule el valor final de la prima mensual de un seguro de mascota y el valor final del chip de identificación.

# Valores base:

# Prima mensual: $22.000
# Chip: $9.000
# Reglas de descuento de la prima:

# Peso >= 20 kg:
# Cobertura A o B → 16%
# Cobertura C o D → 10%
# 8 <= peso < 20 kg:
# Cobertura A o B → 10%
# Cobertura C o D → 6%
# Menor a 8 kg → sin descuento.
# Reglas del chip:

# Cobertura A o B → 12% descuento.
# Si además el peso >= 15 kg → 6% adicional.
# Debe mostrar ambos valores finales.

# Input Esperado
# 25
# A

# Output Esperado
# Prima mensual: 18480
# Chip: 7444

peso = int(input("¿Cúal es su peso?: "))
cobertura = input("¿Qué cobertura tiene?: ")

prima_mensual = 22000
chip = 9000

if peso >= 20:
    if cobertura == "A" or cobertura == "B":
        prima_mensual *= 0.84
    elif cobertura == "C" or cobertura == "D":
        prima_mensual *= 0.90
    else:
        print("Las coberturas son de A hasta la D")
elif 8 <= peso < 20:
    if cobertura == "A" or cobertura == "B":
        prima_mensual *= 0.90
    elif cobertura == "B" or cobertura == "D":
        prima_mensual *= 0.94
    else:
        print("Las coberturas son de A hasta la D")
else:
    print("Ingrese un valor correctamente")

#cobertura

if cobertura == "A" or cobertura == "B":
    chip *= 0.88
    if peso >= 15:
        chip *= 0.94
else:
    chip *= 100

print(f"Prima mensual: {int(prima_mensual)}")
print(f"Chip: {int(chip)}")

