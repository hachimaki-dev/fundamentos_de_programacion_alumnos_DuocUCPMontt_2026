Notas = 3.4
Asistencia = 85

if Asistencia > 80 :
    Notas = Notas + 0.5 
    print (f"Tu nota actual es {Notas}")

    if Notas >=  4.0 :
        print ("Aprobado")
    
    elif Notas > 3.5 or Notas > 3.9 :
        print ("Examen")

    else :
        print ("Reprobado")

    