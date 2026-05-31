prestamos_activos = 0
equipos_disponibles = 60
while True:
   try:
        print("=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")
        print("1. Ver equipos disponibles")
        print("2. Prestar equipo(s)")
        print("3. Recibir devolución")
        print("4. Ver historial de préstamos activos")
        print("5. Salir")
        opcion_elegida = int(input("que opcion quieres elegir "))
   
        if opcion_elegida == 1:
           print(f"los equipos disponibles son {equipos_disponibles} tablets")
        elif opcion_elegida == 2:
           NumeroDeEquiposASacar = int(input("cuantas tables quieres sacar "))
           if NumeroDeEquiposASacar <= 0:
                print("Debes ingresar un número mayor a cero.")
           elif NumeroDeEquiposASacar > equipos_disponibles:
               print("no puedes sacar mas tablets del stock maximo")
           else:
               equipos_disponibles -= NumeroDeEquiposASacar
               prestamos_activos += NumeroDeEquiposASacar
               print(f"haz sacado {NumeroDeEquiposASacar} tablets")
        elif opcion_elegida == 3:
            tables_a_devolver = int(input("cuantas tablets quieres devolver? "))
            if tables_a_devolver <=0:
                print("tiene que ser un numero entero positivo")

            elif tables_a_devolver > prestamos_activos or (equipos_disponibles + tables_a_devolver > 60):
                print("no puedes devolver mas de los equipos que estan prestados ni tampoco mas del estock maximo")
            
            
            else:
             equipos_disponibles += tables_a_devolver
             prestamos_activos -= tables_a_devolver
             print(f"devolviste {tables_a_devolver} tablets")
             print(f"hay {equipos_disponibles} tablets en total")
        elif opcion_elegida == 4:
            print(f"tu historial es de {prestamos_activos} tables")
        elif opcion_elegida == 5:
            print("Gracias por utilizar el sistema. Hasta pronto.")
            break
        else:
            print("solo puedes eligir un numero de 1 al 5")
   except ValueError:
        print("Solo se puede seleccionar un número válido. Intenta de nuevo.")
    