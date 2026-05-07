print("App para calcular calorías ")
minuto = 0
kcal_quemadas = 0
while kcal_quemadas < 300:
    minuto += 1
    if minuto <= 10:
        kcal_quemadas += 20
    else:
        kcal_quemadas += 10
        ("Debido a que llevas rato trotando te cansaste, ahora vas más despacio.")
    print(f"Después de {minuto} minutos trotando llevas {kcal_quemadas} kilocalorias quemadas")

print(f"Te demoraste {minuto} minutos en quemar 300 kcal.")