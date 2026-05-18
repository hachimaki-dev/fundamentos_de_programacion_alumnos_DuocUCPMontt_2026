nota = 3.6

asistencia = 85

if asistencia >= 80:
    nota += 0.5

revisar_estado = input("¿Desea revisar su estado? (s/n): ")

if revisar_estado.lower() == 's':
    if nota >= 4.0:
        print(f"¡Aprobado")
    elif nota >= 3.5 and nota < 3.9:
        ir_a_examen = input("¿Ir a examen? (s/n): ")

        if ir_a_examen.lower() == 's':
            print("Dirigiéndose al examen...")
            
        else:
            print("Reprobado")