edad_ingresada = int(input("Ingrese su edad\n"))
pregunta_inscripcion = input("esta usted inscrito? (si/no)\n")
esta_inscrito = False

if pregunta_inscripcion == "si":
    esta_inscrito = True
elif pregunta_inscripcion == "no":
    esta_inscrito = False

if edad_ingresada >= 18 and esta_inscrito == True:
    print("Inscripcion aceptada")
elif edad_ingresada < 18:
    print("Debe de ser mayor de edad para poder inscribirse")
else:
    print("Inscripcion rechazada")
print("Fin del proceso")