


edad_de_la_persona = int(input("ingrese su edad\n :"))
inscrita_previamente = input("esta inscrita previamente ( responda SI o NO) \n :")

if edad_de_la_persona >= 18:
    if inscrita_previamente == "SI" or inscrita_previamente == "si":
        print("inscripción aceptada")
    elif inscrita_previamente == "NO" or inscrita_previamente == "no":
        print("inscripcion rechazada")
    else :
        print("inscripcion rechazada")
elif edad_de_la_persona < 18 :
    print("Debe ser mayor de edad para poder inscribirse")
print("******Fin del proceso********")

