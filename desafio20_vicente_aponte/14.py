alumnos = [{'nombre': 'Ana', 'nota': 5.0}, {'nombre': 'Luis', 'nota': 3.0}]
aprobados = ""
for i in alumnos:
    print(i["nota"])
    if i["nota"] >= 4.0:
        aprobados = aprobados + 1
print(aprobados)