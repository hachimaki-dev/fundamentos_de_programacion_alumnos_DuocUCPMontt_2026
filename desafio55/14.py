nota_inicial= 3.6
asistencia= 85

if asistencia >= 80:
    nota_final= nota_inicial + 0.5
    if nota_final >= 4.0:
        print("Estas aprobado")
    elif nota_final >= 3.5 and nota_final < 4.0:
        print("Vas a examen")
    else:
        print("Reprobado")