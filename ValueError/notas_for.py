# Habilidad que desarrollas: Primero validar cuántas veces iterar, luego iterar exactamente esa cantidad de veces, validando cada dato dentro del loop.
# Ejercicio 10 — Registro de notas de un curso universitario
# El docente ingresa cuántos estudiantes tiene en su curso (entero positivo). Luego, para cada estudiante, ingresa su nota (entero de 1 a 7, validado).
# Al final muestra:
# Cuántos aprobaron (nota ≥ 4)
# Cuántos reprobaron (nota < 4)
# El promedio del curso
# Estructura que debes aplicar:

# 1. Validar N (cantidad de estudiantes)
# 2. for i in range(N):
# validar nota
# clasificar y contar
# 3. Mostrar resumen
suma_notas = 0
notas_de_curso = {
    "aprobados": 0,
    "reprobados": 0,
}
while True:
    try:
        cantidad_de_estudiantes = int(input("Ingrese la cantidad de estudiantes que tiene en el curso \n"))
        if cantidad_de_estudiantes <= 0:
            print("Debe ingresar un numero positivo")
            continue
        else:
            for nota_estudiante in range(cantidad_de_estudiantes):
                nota_ingresada_estudiantes = int(input("Ingrese la nota del estudiante (1 a 7 sin decimales)\n"))
                if nota_ingresada_estudiantes < 1 or nota_ingresada_estudiantes > 7:
                    print("Nota invalida debe ser de 1 al 7")
                    continue
                if nota_ingresada_estudiantes >= 4:
                    print("aprobado")
                    notas_de_curso["aprobados"] += 1
                elif nota_ingresada_estudiantes < 4:
                    print("reprobado")
                    notas_de_curso["reprobados"] += 1
                suma_notas += nota_ingresada_estudiantes
            promedio_notas_del_curso = suma_notas / cantidad_de_estudiantes
            print(f"Promedio del curso: {promedio_notas_del_curso}")
            print(f"Resumen en general: {notas_de_curso}")
            break
    except Exception as error_de_lectura:
        print(f"Error de : {error_de_lectura}")