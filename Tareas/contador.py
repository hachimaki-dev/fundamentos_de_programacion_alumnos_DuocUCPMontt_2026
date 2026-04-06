Estudiantes = 0
A_Favor = 0
En_Contra = 0
contador = 0
bandera = True

print("Bienvenido al contador de votos estudiantiles")
Estudiantes = int(input("¿Cuantos estudiantes van a votar?"))
while bandera:
    contador = contador + 1
    print("Tienes que votar A FAVOR (A) o EN CONTRA (C)")
    eleccion = input(f"Cual es la elecciòn del estudiante {contador}")
    if eleccion == "A":
        print(f"El estudiante{contador} a votado A FAVOR")
        A_Favor = A_Favor + 1
    elif eleccion == "C":
        print(f"El estudiante{contador} a votado EN CONTRA")
        En_Contra = En_Contra + 1
    else:
        print("El caracter es INCORRECTO")
        contador = contador - 1
    if contador == Estudiantes:
        print("Se ha terminado el conteo")
        break
if A_Favor > En_Contra:
    print("FELICIDADES, A GANADO A FAVOR")
    import sys
    sys.exit ()
if A_Favor < En_Contra:
    import sys
    sys.exit ()
    print("FELICIDADES A GANADO EN CONTRA")