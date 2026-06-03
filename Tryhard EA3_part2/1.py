#Contexto: Un sistema escolar necesita clasificar notas de alumnos.
#Lo que debe hacer el programa: Primero pregunta cuántos alumnos hay.
#Luego, para cada alumno, pide su nota (un número entre 1 y 100).
#Si la nota es mayor a 59, muestra "Aprobado"; si es 59 o menor, muestra "Reprobado".
#Al terminar todos los alumnos, muestra cuántos aprobaron y cuántos reprobaron: "Resultado: X aprobados y Y reprobados."


cantidad_alumnos=0

while True:
    try:
        cantidad_alumnos=int(input("¿Cuantos alumnos son? "))
        if cantidad_alumnos > 0:
            break
        print("Por favor, ingrese un número positivo de alumnos.")
    except ValueError:
        print("Entrada invalida.")

aprobados=0
reprobados=0

for _ in range(cantidad_alumnos):
    while True:
        try:
            nota=int(input(f"¿Que nota tuvo el alumno {_+1}? "))
            if nota >=1 and nota <=100:
                break
            print("La nota debe ser entre 1 y 100")
        except ValueError:
            print("Entrada invalida.")
    
    if nota > 59:
        aprobados+=1
        print("Aprobado")
    else:
        reprobados+=1
        print("Reprobado")
        
print(f"Resultado: {aprobados} aprobados y {reprobados} reprobados.")
