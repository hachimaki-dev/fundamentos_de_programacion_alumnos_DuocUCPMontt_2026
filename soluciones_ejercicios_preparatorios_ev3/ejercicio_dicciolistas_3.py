estudiante_1 = {"Nombre":"Juan","Edad":"18","Notas":[2.3,5.0,4.5]}
estudiante_2 = {"Nombre":"Rosa","Edad":"17","Notas":[7.0,5.9,6.5]}
estudiante_3 = {"Nombre":"Ramón","Edad":"18","Notas":[2.3,1.0,3.8]}
lista_de_estudiantes = [estudiante_1,estudiante_2,estudiante_3]
contador_de_estudiantes = len(lista_de_estudiantes)
contador_deciclo = 0
for estudiante in lista_de_estudiantes:
    print(estudiante.get("Nombre"))
    cantidad_notas = len(estudiante.get("Notas"))
    promedio = sum(estudiante["Notas"])/cantidad_notas
    promedio = round(promedio,2)
    estudiante["Promedio"] = promedio
    
    if estudiante["Promedio"] >= 4.0:
        print("APROBADO")
    else:
        print("REPROBADO")    
while True:
    nombre_alumno_a_buscar = input(f"Ingrese un nombre de algun alumno para ver información: ").strip()
    for estudiante in lista_de_estudiantes:
        contador_deciclo += 1
        if estudiante["Nombre"] == nombre_alumno_a_buscar:
            print(estudiante.items())
            print(f"Nombre:{(estudiante.get("Nombre"))} Promedio:{estudiante.get("Promedio")} Notas: {estudiante.get("Notas")} Edad: {estudiante.get("Edad")}")
        elif nombre_alumno_a_buscar not in estudiante["Nombre"] and contador_de_estudiantes == contador_deciclo:
            print("Alumno no encontrado")
           
