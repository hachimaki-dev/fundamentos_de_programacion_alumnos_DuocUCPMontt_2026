classification = {
    "critic": 0,
    "normal": 0,
    "low": 0
}

for i in range(5):
    try:
        degree = float(input(f"Temperatura {i + 1} (C°): "))
    except ValueError:
        print("Error: Ingresa un número entero o decimal")

    if degree > 80:
        classification["critic"] += 1
    elif degree >= 50 and degree <= 80:
        classification["normal"] += 1
    else:
        classification["low"] += 1

print(f"Temperaturas críticas: {classification.get("critic")}")
print(f"Temperaturas normales: {classification.get("normal")}")
print(f"Temperaturas bajas: {classification.get("low")}")