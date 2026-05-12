# Valores base
prima_mensual = 22000
chip = 9000
peso = 25
cobertura = "A"


if peso >= 20:
    if cobertura == "A" or cobertura == "B":
        prima_mensual *= 0.84  
    elif cobertura == "C" or cobertura == "D":
        prima_mensual *= 0.90  

elif 8 <= peso < 20:
    if cobertura == "A" or cobertura == "B":
        prima_mensual *= 0.90  
    elif cobertura == "C" or cobertura == "D":
        prima_mensual *= 0.94  

else:
    print("Sin descuento en la prima (peso menor a 8kg).")

if cobertura == "A" or cobertura == "B":
    chip *= 0.88 
    
    if peso >= 15:
        chip *= 0.94

print(prima_mensual)
print(chip)