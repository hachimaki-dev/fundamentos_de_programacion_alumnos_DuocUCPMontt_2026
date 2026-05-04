#Crea una lista llamada alumnos que contenga estos dos diccionarios:
#{'nombre': 'Ana', 'nota': 5.0}
#{'nombre': 'Luis', 'nota': 3.0}
#Luego, cuenta cuántos alumnos tienen una nota mayor o igual a 4.0 y guarda ese valor en una variable llamada aprobados. Imprime aprobados.
alumnos = {"nombre": "Ana", "nota": 5.0} , {"nombre": "Luis", "nota": 3.0}
aprobados = 0 
for alumno in alumnos:
    if alumno ["nota"] >= 4.0:
        aprobados += 1
        print(aprobados)