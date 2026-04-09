print("Smart Watch Activity Tracker")
#Monitorear tu actividad fisica en 7 dias.
print("¡Es hora de Registrar tus kilometros diarios!")
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
total = 0

for semana in dias :
    print(f"Es el dia {semana}")
    
    km = int(input("¿Cuántos km recorriste el día de hoy?"))
    

    if km >= 0 :
        print(f"Recorriste {km} km el día {semana}")
    else:
        print("Dia saltado")
    total += km

if total >= 30 :
    print(f"Felicidades, recorriste {total} km, META SEMANAL CUMPLIDA, eres un atleta")
elif total <= 30 :
    print(f"Sigue intentanto llevas {total} km, ¡Tu puedes!")
        

