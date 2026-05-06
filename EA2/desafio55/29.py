
minuto = 0
kcal = 300

while kcal >= 0:
    if minuto <= 10:
        minuto += 1
        kcal -= 20
    else:
        minuto += 1
        kcal -= 10
print(f"Tardaste {minuto} minutos")