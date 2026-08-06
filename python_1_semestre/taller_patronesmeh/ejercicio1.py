"""while True:
    try:
        edad = int(input("ingresa tu edad : \n"))
        if edad <0:
            print("entrada invalida Ingresa un número entero positivo.")
        else:
            print(f"Edad registrada: {edad} años.")
            break
    except ValueError:
        print("ingresa la wea con numeros normales ")"""
#ejercicio2:
"""while True:
    try:
        cantidad_alumnos_usuario = int(input("ingresa la cantidad de alumnos :\n"))
        if cantidad_alumnos_usuario > 0:
            break
        print("ingresa un valor mayor que 0")
    except ValueError:
        print("entrada invalida")
aprobados = 0
reprobados = 0
for i in range(cantidad_alumnos_usuario):
    while True:
        try:
            nota = float(input(f"ingresa la nota {i+1} "))
            if nota > 0 and nota <= 100:
                break
            print("la nota tiene que estar entre 1 y 100")
        except ValueError:
            print("entrada invalida")

    if nota >= 59:
        print("aprobado")
        aprobados +=1
    else:
        print("reprobado")
        reprobados +=1
print(f"cantidada de aprobados : {aprobados} , cantidad de reprobados : {reprobados}")"""
#ejercicio3:
"""atletas_elite = 0
atletas_regular = 0
while True:
    try:
        numero_atletas = int(input("ingresa la cantidad de atletas: "))
        if numero_atletas >0:
            break
        print("ingresa un numero mayor a 0")
    except ValueError:
        print("ingresa un numero valido")
for atleta in range(numero_atletas):
    while True:
        
        codigo_por_cada_atleta = input(f"ingresa el codigo por c/u de los atletas {atleta+1}").strip()
        if " "  in codigo_por_cada_atleta or len(codigo_por_cada_atleta) <5:
            print("ingresa el dato de nuevo sin espacios y la casilla vacia minimo 5 letras")
        else:
            break
            
        
    while True:
        try:
            puntaje_rendimiento = int(input("ingresa el puntaje de rendimiento : \n"))
            if puntaje_rendimiento >0:
                break
            
        except ValueError:
            print("ingresa un numero valido")
if puntaje_rendimiento >70:
    print("atleta elite")
    atletas_elite +=1
else:
    print("atleta regular")
    atletas_regular +=1
print(f"cantidad de atletas de elite: {atletas_elite}\n la cantidad de atletas regulatr son: {atletas_regular}")"""
#ejercicio 4
biblioteca = 30# cantidad de libros disponible
def menu():
    print("opciones: 1) Muestra cuántos libros queda")
    print("2) Préstamo: pide cuántos libros prestar y los descuenta de los disponibles (no se pueden prestar más de los que hay)")
    print("3) Devolución: pide cuántos libros devolver y los suma a los disponibles (no puede pasar de 30).")
    print("4) Muestra un resumen: cuántos libros se prestaron en total menos los devueltos.")
    print("5) Sale del programa.")

