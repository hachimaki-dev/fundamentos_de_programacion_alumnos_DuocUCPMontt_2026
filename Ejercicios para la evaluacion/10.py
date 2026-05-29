flag = True
while flag:
    try:
        cantidad_de_estudiantes = int(input("Profesor, ¿cuantos alumnos tiene su curso? "))
        if cantidad_de_estudiantes <= 0:
            print("Ingrese un número entero positivo de estudiantes.")
        else:
            print(f"La cantidad de estudiantes es de {cantidad_de_estudiantes}.")
            flag = False
    except ValueError:
        print("Ingrese números, no letras, puntos u otros caracteres especiales.")
notas_estudiantes = []
notas_azules = []
notas_rojas = []

for alumno in range(1,cantidad_de_estudiantes+1):
    try:
        nota_por_estudiante = float(input(f"Ingrese nota del alumno n°{alumno}: "))
        if nota_por_estudiante > 7:
            print("No es posible ingresar notas sobre 7.")
        elif nota_por_estudiante <= 1.0:
            print("No es posible ingresar notas debajo de 0.")
        else:
            notas_estudiantes.append(nota_por_estudiante)
    except ValueError:
        print("Ingrese notas válidas.")

print(notas_estudiantes)