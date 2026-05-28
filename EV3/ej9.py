classification = {
    "approved": 0,
    "manual": 0,
    "rejected": 0
}

next = False

for i in range(8):
    while True:
        try:
            score = int(input(f"Ingresa el score crediticio {i + 1}: "))
            next = True
        except ValueError:
            print("Error: Ingresa un número entero entre 1 y 1000")

        if next:
            if score >= 0 and score <= 1000:
                break
            else:
                print("Error: Ingresa un número entero entre 1 y 1000")

    if score > 750:
        classification["approved"] += 1
    elif score >= 500 and score <= 750:
        classification["manual"] += 1
    else:
        classification["rejected"] += 1

print(f"Aprobados automáticamente: {classification.get("approved")}")
print(f"Pendientes de revisión manual: {classification.get("manual")}")
print(f"Rechazados: {classification.get("rejected")}")