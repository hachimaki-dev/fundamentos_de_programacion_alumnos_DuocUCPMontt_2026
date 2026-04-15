print("Bienvenido a la insripción de taller gratuito, porfavor rellenar la siguiente informacion:")

edad_ingresada = int(input("Ingrese su edad: "))
inscrito_con_anterioridad = input("Se ha inscrito previamente (SI o NO): ")

if edad_ingresada < 18:
    print("Debe ser mayor de edad para poder inscribirse.")
elif edad_ingresada >= 18:
    print("Inscripción aceptada")
else:
    print("Inscripcion rechazada")

print("Fin del proceso")