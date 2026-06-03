estudiante_1 = {"Nombre":"Juan","Edad":"18","Notas":[2.3,5.0,4.5]}
estudiante_2 = {"Nombre":"Rosa","Edad":"17","Notas":[7.0,5.9,6.5]}
estudiante_3 = {"Nombre":"Ramón","Edad":"18","Notas":[2.3,1.0,3.8]}
lista_de_estudiantes = [estudiante_1,estudiante_2,estudiante_3]
for estudiante in lista_de_estudiantes:
    print(estudiante.get("Nombre"))
    cantidad_notas = len(estudiante.get("Notas"))
    promedio = sum(estudiante["Notas"])/cantidad_notas
    promedio = round(promedio,2)
    estudiante["Promedio"] = promedio
    print(estudiante.get("Promedio"))

        
