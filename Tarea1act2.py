#Menú
while True: #Ponemos la condición será siempre True.
    print("---MENÚ---")
    print("1. Saludar.")
    print("2. Contar historia.")
    print("3. Salir.")

    opcion = int(input("Porfavor elija su opción. "))
    if opcion == 1:
        print("Hola usuario, ¿como estas?")
    elif opcion == 2:
        print("Habia una vez un caballero que fue a salvar a una princesa.")
        print("Y murió.")
    elif opcion == 3:
        print("Adiós usuario. :)")
        break #Aqui rompemos el ciclo del while.
    else:
        print("Por favor escoja una opción válida.")
print("----Fin Del Programa----")