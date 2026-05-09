#Valores base
prima = 22000
chip = 9000

#inputs
print("****** Bienvenido a Veterinaria Cholito ******\n")
peso = float(input("Ingresa el peso de tu mascota (en kg): "))
print("\n¿Escoge un plan de cobertura?")
print("- Cobertura A")
print("- Cobertura B")
print("- Cobertura C")
print("- Cobertura D")
cobertura = input("Ingresa la letra de tu plan de cobertura: ").upper()

#Descuento de la prima
if peso >= 20:
    if cobertura == 'A' or cobertura == 'B':
        prima -= (prima * 0.16)
    elif cobertura == 'C' or cobertura == 'D':
        prima -= (prima * 0.1)
elif 8 <= peso < 20:
    if cobertura == 'A' or cobertura == 'B':
        prima -= (prima * 0.1)
    elif cobertura == 'C' or cobertura == 'D':
        prima -= (prima * 0.06)
elif peso < 8:
    prima 

#Descuentos chips
if cobertura == 'A' or cobertura == 'B':
    chip -= (chip * 0.12)

if peso >= 15:
    chip -= (chip * 0.06)


print(f"Prima mensual: ${int(prima)}")
print(f"Chip: ${int(chip)}")