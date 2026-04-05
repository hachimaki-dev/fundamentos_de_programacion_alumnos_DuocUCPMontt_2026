edad= int(input("Ingrese su edad: "))
dificultad= input("Tiene dificultad para respirar: ")
nivel_dolor= int(input("Califique su nivel de dolor del 1 al 10: "))

if dificultad== "SI":
    print("¡URGENCIAS NIVEL 1!, pase inmediatamente.")
elif dificultad=="NO":
    if edad>60 and nivel_dolor>7:
        print("URGENCIAS NIVEL 2, pase pronto.")
    elif nivel_dolor<4:
        print("Urgencias nivel 5, puede irse a su casa o a un consultorio.")
    else:
        print("Urgencias nivel 3-4, tome asiento por favor.")