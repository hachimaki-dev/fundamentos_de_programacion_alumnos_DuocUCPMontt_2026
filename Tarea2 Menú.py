#Menú
while True: 
    print("**MENÚ**")
    print("1. Saludo cordial")
    print("2. Contar chiste")
    print("3. Contar Historia")
    print("4. Salir")
    
    opciones = int(input("A su favor, elija a su preferencia"))
    if opciones == 1:
        print("Estimado, espero que este mensaje le encuentre muy bien. Es un placer dirigirme a usted con el mayor respeto y consideración")
    elif opciones == 2 :
        print("¿Qué hace una abeja en el gimnasio?")
        print("¡Zum-ba!")
    elif opciones == 3 :
        print("Un hombre entró a una librería y preguntó: ¿Tiene libros sobre el cansancio?. El vendedor respondió: Sí, pero están agotados.")
    elif opciones == 4 :
        print("Me despido cordialmente, agradeciendo su voluntad de interactuar con mi menú, muchas gracias.")
        break

    else:
        print("Porfavor de elegir una de las opciones correspondientes.")
        print("***FIN DE LA PROGRAMACIÓN***")
      