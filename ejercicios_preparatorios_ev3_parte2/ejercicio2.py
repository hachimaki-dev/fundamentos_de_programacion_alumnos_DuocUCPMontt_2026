while True:
    try:
        cantidad_alumnos = int(input("¿Cuantos alumnos hay en el curso?: "))
        if cantidad_alumnos <= 0:
            print("Error: Ingresa un número entero positivo.")
        else:
            break
    except ValueError:
        print("Dato invalido: Solo se permiten numeros enteros positivos.")

aprobado = 0
reprobado = 0

for i in range(cantidad_alumnos):
    while True:
        try:
            nota_alumno = int(input(f"Ingrese la nota de alumo {i+1}: "))
            if 1 <= nota_alumno <= 100:
                break
            print("La nota debe estar entre 1 y 100.")
        except ValueError:
            ("Ingrese una nota entera valida.")

        
    if nota > 59:
        print("Aprobado")
        aprobado += 1
    else:
        print("Reprobado")
        reprobado += 1
    
print(f"Resultado: {aprobado} aprobados y {reprobado} reprobados.")