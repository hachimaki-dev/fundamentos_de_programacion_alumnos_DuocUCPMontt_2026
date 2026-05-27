#Desarrolle un programa que calcule el valor final de la prima mensual de un seguro de mascota y el valor final del chip de identificación.

#Valores base:

#Prima mensual: $22.000
#Chip: $9.000
#Reglas de descuento de la prima:

#Peso >= 20 kg:
#Cobertura A o B → 16%
#Cobertura C o D → 10%
#8 <= peso < 20 kg:
#Cobertura A o B → 10%
#Cobertura C o D → 6%
#Menor a 8 kg → sin descuento.
#Reglas del chip:

#Cobertura A o B → 12% descuento.
#Si además el peso >= 15 kg → 6% adicional.
#Debe mostrar ambos valores finales.
prima_mensual = 22000
chip = 9000
peso = int(input("ingrese el peso de la mascota: "))
cobertura = input("ingrese cobertura (A,B,C,D):")
if peso >= 20 :
    if cobertura == "A" or cobertura == "a" or cobertura == "B" or cobertura == "b":
        prima_mensual *= 0.84
    elif cobertura == "C" or cobertura == "c" or cobertura == "D" or cobertura == "d":
        prima_mensual *= 0.90
elif 8 <= peso < 20 :
    if cobertura == "A" or cobertura == "a" or cobertura == "B" or cobertura == "b":
        prima_mensual *= 0.90
    elif cobertura == "C" or cobertura == "c" or cobertura == "D" or cobertura == "d":
        prima_mensual *= 0.94
elif peso < 8:
    print("sin descuento")
if cobertura == "A" or cobertura == "a" or cobertura == "B" or cobertura == "b":
    chip *= 0.88
    if peso >= 15:
        chip *= 0.94
print(f"mesual: {prima_mensual} \n chip : {chip}")
