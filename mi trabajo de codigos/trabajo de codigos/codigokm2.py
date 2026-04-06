print("\"Bienvenido a tu smarwach activty  tracker personal donde registraremos tu pregreso diario de km recorridos y le daremos un total semanal\"")
print("\nintruccione de uso: ")
print("\n\t -Ingresar tus kilometros diariamente.\n\t -Si un dia fallas o te lesionas deberás ingresa -1 para que ese dia se registre como día saltado\n")
dias = 1
total = 0

while dias <= 7 :
    print(f"\n**Es el dia {dias}**")    
    km =int(input("Cuantos km hiciste el dia de hoy?"))
    if km >= 0 :
        print(f"hoy recorriste {km} km")
        total += km
    elif km == -1:
        print("Dia saltado")

        
    dias += 1
    
print(f"\n**Recorriste {total} km esta semana**\n")
if total >= 30:
    print(f"¡Felicidades cumpliste tu meta semanal con {total} km recorridos\n!")
elif total < 30:
    print(f"Te falto para llegar a tu meta semanal 🥺​​ esta semana hiciste {total} km intentalo mejor la proxima semana\n")