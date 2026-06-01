prestamos_activos = 0
equipos_disponibles = 60
historial_prestamos = []  # <--- NUESTRA LISTA

while True:
    try:
        print("\n=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")
        print("1. Ver equipos disponibles")
        print("2. Prestar equipo(s)")
        print("3. Recibir devolución")
        print("4. Ver historial de préstamos activos")
        print("5. Salir")
        opcion_elegida = int(input("¿Qué opción quieres elegir? "))
   
        if opcion_elegida == 1:
            print(f"Los equipos disponibles son {equipos_disponibles} tablets")
            
        elif opcion_elegida == 2:
            NumeroDeEquiposASacar = int(input("¿Cuántas tablets quieres sacar? "))
            if NumeroDeEquiposASacar <= 0:
                print("Debes ingresar un número mayor a cero.")
            elif NumeroDeEquiposASacar > equipos_disponibles:
                print("No puedes sacar más tablets del stock máximo.")
            else:
                nombre_usuario = input("Introduce el nombre del estudiante: ") # <--- Pedimos nombre
                
                equipos_disponibles -= NumeroDeEquiposASacar
                prestamos_activos += NumeroDeEquiposASacar
                
                # <--- NUESTRO DICCIONARIO guardado en la LISTA
                registro = {"usuario": nombre_usuario, "cantidad": NumeroDeEquiposASacar}
                historial_prestamos.append(registro)
                
                print(f"Has sacado {NumeroDeEquiposASacar} tablets para {nombre_usuario}")
                
        elif opcion_elegida == 3:
            tables_a_devolver = int(input("¿Cuántas tablets quieres devolver? "))
            if tables_a_devolver <= 0:
                print("Tiene que ser un número entero positivo.")
            elif tables_a_devolver > prestamos_activos or (equipos_disponibles + tables_a_devolver > 60):
                print("No puedes devolver más de los equipos prestados ni superar el stock máximo.")
            else:
                equipos_disponibles += tables_a_devolver
                prestamos_activos -= tables_a_devolver
                print(f"Devolviste {tables_a_devolver} tablets.")
                print(f"Hay {equipos_disponibles} tablets en total en bodega.")
                
        elif opcion_elegida == 4:
            # <--- NUESTRO BUCLE FOR para leer los datos
            print("\n--- HISTORIAL DE PRÉSTAMOS ---")
            if not historial_prestamos:
                print("No hay registros de préstamos.")
            else:
                for registro in historial_prestamos:
                    print(f"• {registro['usuario']} se llevó {registro['cantidad']} tablets.")
                    
        elif opcion_elegida == 5:
            print("Gracias por utilizar el sistema. Hasta pronto.")
            break
        else:
            print("Solo puedes elegir un número del 1 al 5.")
    except ValueError:
        print("Solo se puede seleccionar un número válido. Intenta de nuevo.")