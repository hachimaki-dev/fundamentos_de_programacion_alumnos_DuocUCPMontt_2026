
#VARIABLES
edad = int(input("Ingrese su Edad: "))
inscripcion = input("\n¿Incripción Previa? (SI/NO)")
#COMPARADOR con puerta AND (Incluidas diferentes variables del string "si")
if edad >= 18 and (inscripcion == "SI" or inscripcion == "si" or inscripcion == "Si" or inscripcion == "sI"): 
    print("\nInscripción Aceptada")
elif edad < 18:
    print("\nDebe ser mayor de edad para poder inscribirse")
else:
    print("\nInscripción Rechazada")

print("\nFin del Proceso")