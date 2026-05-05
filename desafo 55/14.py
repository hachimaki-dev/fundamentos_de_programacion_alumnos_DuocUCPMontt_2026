nota = float(input("Cual es tu nota: "))
asistencia = int(input("Cuanta asistencia tienes: "))

if asistencia >= 80: 
    nota = nota + 0.5 

    if nota >= 4.0: 
        print("Aprobado")
    
    elif nota <= 3.9: 
        print("Examen")
    elif nota >= 3.5: 
        print("Examen")
    else:
        print("Reprobado")