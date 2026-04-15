Edad_usuario = input("Ingrese su edad:\n")
Inscripcion_previa = input("¿Ha estado inscrito anteriormente?\n1. Si\n 2. No\n")

if Edad_usuario >= "18":
    if Inscripcion_previa == "1":
        print("Inscripción Aceptada")
    elif Inscripcion_previa == "2":
        print("Inscripción rechazada")
elif Edad_usuario <= "17":
    print("Debe ser mayor de edad para poder inscribirse")