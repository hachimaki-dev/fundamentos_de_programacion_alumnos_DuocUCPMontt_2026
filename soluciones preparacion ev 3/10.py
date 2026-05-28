while True :
    try :
        cantidad_estudiantes = int(input("Ingrese cuántos estudiantes tiene su curso: "))

        if cantidad_estudiantes <= 0 :
            print("Ingrese un valor positivo.")
        else :
            break
    except ValueError :
        print("Ingrese un valor numérico positivo.")

for i in range(cantidad_estudiantes) :
    try :
        nota_alumno = float(input("Ingrese la nota para el alumno (entre 1 y 7)"))
    except ValueError :
        print("ERROR. Ingrese un valor entre 1 y 7.")