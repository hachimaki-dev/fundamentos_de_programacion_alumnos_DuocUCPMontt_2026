print("🔬 ESTACIÓN CIENTÍFICA ANTÁRTICA")
print("Sistema de Monitoreo Ambiental")

while True:
    try:
        num_lecturas = int(input("¿Cuántas lecturas registrar? "))
        if num_lecturas > 0:
            break
        print("Debe ser mayor a 0.")
    except ValueError:
        print("Ingresa un número entero.")

lecturas = []
alertas = 0
temp_min = 50
temp_max = -60
suma_temps = 0

for i in range(num_lecturas):
    print(f"\n--- Lectura {i+1} ---")

    while True:
        hora = input("Hora de la lectura: ").strip()
        if len(hora) > 0:
            break
        print("La hora no puede estar vacía.")

    while True:
        try:
            temp = int(input("Temperatura (°C): "))
            if -60 <= temp <= 50:
                break
            print("Debe estar entre -60 y 50.")
        except ValueError:
            print("Ingresa un entero válido.")

    es_alerta = False
    if temp <= -20:
        print("⚠️ ALERTA: Temperatura crítica")
        alertas += 1
        es_alerta = True

    if temp < temp_min:
        temp_min = temp
    if temp > temp_max:
        temp_max = temp

    registro = {"hora": hora, "temp": temp, "alerta": es_alerta}
    lecturas.append(registro)

promedio = suma_temps / num_lecturas # la variable no suma, no se le agrege nada

print(f"\n🔬 INFORME DEL DÍA")
print(f"Lecturas registradas: {num_lecturas}")
print(f"Temperatura mínima: {temp_min}°C")
print(f"Temperatura máxima: {temp_max}°C")
print(f"Promedio: {promedio}°C")
print(f"Alertas críticas: {alertas}")

print(f"\n--- Detalle de Alertas ---")
for r in lecturas:
    if r["alerta"]:
        print(f"Hora: {r['hora']} | Temp: {r['temp']}°C")