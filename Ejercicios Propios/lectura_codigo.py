print("🏙️ COLONIA TERRANOVA — Sistema de Gestión")

colonos = []

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Registrar colono")
    print("2. Buscar colono")
    print("3. Reporte de la colonia")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\n--- Registro de Colono ---")

        while True:
            nombre = input("Nombre: ").strip()
            if len(nombre) > 0:
                break
            print("El nombre no puede estar vacío.")

        while True:
            try:
                edad = int(input("Edad (18-65): "))
                if 18 <= edad <= 65:
                    break
                print("La edad debe estar entre 18 y 65.")
            except ValueError:
                print("Ingresa un número entero.")

        especialidades_validas = ["ingenieria", "medicina", "ciencia"]
        while True:
            especialidad = input("Especialidad (ingenieria/medicina/ciencia): ").strip().lower()
            if especialidad in especialidades_validas:
                break
            print("Especialidad no válida. Elige: ingenieria, medicina o ciencia.")

        colono = {"nombre": nombre, "edad": edad, "especialidad": especialidad}
        colonos.append(colono)
        print(f"✅ Colono {nombre} registrado exitosamente.")

    elif opcion == "2":
        busqueda = input("Nombre del colono a buscar: ").strip()
        encontrado = False

        for c in colonos:
            if c["nombre"].lower() == busqueda.lower(): 
                print(f"\n🔍 Colono encontrado:")
                print(f"   Nombre: {c['nombre']}")
                print(f"   Edad: {c['edad']}")
                print(f"   Especialidad: {c['especialidad']}")
                encontrado = True
                break

        if not encontrado:
            print("Colono no encontrado.") 
            
    elif opcion == "3":
        total = len(colonos)
        if total == 0:
            print("No hay colonos registrados.")
        else:
            print("\n📊 REPORTE DE LA COLONIA")
            
            
            print(f"Total de colonos: {total}")

            ing = 0
            med = 0
            cie = 0
            suma_edades = 0
            
            for c in colonos:
                suma_edades += c["edad"]
                if c["especialidad"] == "ingenieria":
                    ing += 1
                elif c["especialidad"] == "medicina":
                    med += 1
                elif c["especialidad"] == "ciencia":
                    cie += 1

            print(f"Ingeniería: {ing}")
            print(f"Medicina: {med}")
            print(f"Ciencia: {cie}")

            promedio_edad = suma_edades / total
            print(f"Edad promedio: {round(promedio_edad, 1)}")

    elif opcion == "4":
        print("Cerrando sistema. ¡Hasta la próxima misión!")
        break

    else:
        print("Opción no válida. Elige entre 1 y 4.")