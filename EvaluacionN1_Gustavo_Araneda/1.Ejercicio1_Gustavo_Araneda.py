print("Bienvenido al verificador de edad para la inscripción de nuestro taller gratuito.")

edad_usuario = int(input("Por favor, ingrese su edad \nRespuesta: "))
inscripcion_previa = input("¿Usted se ha inscrito previamente?(SI/NO) \nRespuesta: ")

if edad_usuario >= 18:
    if inscripcion_previa == 'SI':
        print("Inscripción aceptada")
    else:
        print("Inscripción rechazada")

elif edad_usuario < 18:
    print("Debe ser mayor de edad para poder inscribirse")

print("Fin del proceso")