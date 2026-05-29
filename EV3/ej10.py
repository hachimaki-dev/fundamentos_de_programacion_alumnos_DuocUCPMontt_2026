classification = {
    "approved": 0,
    "failed": 0
}

grades = []

next = False

while True:
    try:
        quant_students = int(input("Ingrese la cantidad de alumnos: "))
        break
    except ValueError:
        print("Error: Ingresa un número entero positivo")

for i in range(quant_students):
    while True:
        try:
            student_grade = int(input(f"Ingrese la nota del alumno {i + 1}: "))
            next = True
        except ValueError:
            print("Error: Ingresa un número entero positivo")

        if next:
            if student_grade >= 1 and student_grade <= 7:
                break
            else:
                print("Error: Ingresa una nota entre 1 y 7")

    grades.append(student_grade)

    if student_grade >= 4:
        classification["approved"] += 1
    else:
        classification["failed"] += 1

total = 0
for grade in grades:
    total += grade

average = total / len(grades)

print(f"Estudiantes aprobados: {classification.get("approved")}")
print(f"Estudiantes reprobados: {classification.get("failed")}")
print(f"Promedio del curso: {average}")