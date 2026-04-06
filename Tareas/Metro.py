bandera = True
estudiantes = 0
normales = 0
precio_total = 0
print("Bienvenido, este es el Metro de Python")
print("Para pasajeros 'Normales' se pagara $800 CLP")
print("Para estudiantes se pagara $250 CLP")
while bandera:
    print("Estudiantes, $250 CLP")
    print("Normales, $800 CLP")
    respuesta = input("Ingrese la letra 'E' para estudiantes,'N' para normales y 'CORTE' para cortar")
    if respuesta == "E":
        estudiantes = estudiantes + 1
        print(f"Vale, por ahora seria {estudiantes} de pasaje estudiante")
        precio_total = precio_total + 300
    if respuesta == "N":
        normales = normales + 1
        print(f"Vale, por ahora seria {normales} de pasaje normal")
        precio_total = precio_total + 850
    if respuesta == "CORTE":
        print(f"Serian {normales} de Pasaje Normal y {estudiantes} de pasaje de Estudiante ")    
        print(f"El total a pagar seria de ${precio_total}CLP")
        print("Que tenga un buen dia")
        import sys
        sys.exit ()