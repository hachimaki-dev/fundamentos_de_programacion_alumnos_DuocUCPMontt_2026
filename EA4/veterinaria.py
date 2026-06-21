def validar_nombre(nombre):
    """Valida que el nombre no esté vacío ni contenga solo espacios."""
    return len(nombre.strip()) > 0

def validar_especie(especie):
    """Valida que la especie no esté vacía ni contenga solo espacios."""
    return len(especie.strip()) > 0

def validar_peso(peso_str):
    """Valida que el peso sea un número decimal mayor que cero."""
    try:
        peso = float(peso_str)
        return peso > 0
    except ValueError:
        return False

def buscar_animal(lista_animales, nombre_buscar):
    """
    Busca un animal por su nombre (ignorando mayúsculas/minúsculas).
    Retorna el índice si lo encuentra, o -1 si no existe.
    """
    for i, animal in enumerate(lista_animales):
        if animal["nombre"].lower() == nombre_buscar.strip().lower():
            return i
    return -1

def actualizar_alertas(lista_animales):
    """Recorre la lista y actualiza el estado de alerta según el peso."""
    for animal in lista_animales:
        if animal["peso"] < 3.0:
            animal["alerta"] = True
        else:
            animal["alerta"] = False

def main():
    
    animales = []

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Registrar animal")
        print("2. Buscar animal")
        print("3. Eliminar animal")
        print("4. Actualizar alertas")
        print("5. Mostrar animales")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Seleccione una opción: ").strip()

       
        if opcion == "1":
            print("\n--- Registrar Nuevo Animal ---")
            
            nombre = input("Nombre: ")
            if not validar_nombre(nombre):
                print("Error: El nombre no puede estar vacío.")
                continue
                
            especie = input("Especie: ")
            if not validar_especie(especie):
                print("Error: La especie no puede estar vacía.")
                continue
                
            peso_str = input("Peso (kg): ")
            if not validar_peso(peso_str):
                print("Error: El peso debe ser un número decimal mayor que cero.")
                continue
            
            
            nuevo_animal = {
                "nombre": nombre.strip(),
                "especie": especie.strip(),
                "peso": float(peso_str),
                "alerta": False  
            }
            animales.append(nuevo_animal)
            print(f"¡Animal '{nuevo_animal['nombre']}' registrado con éxito!")

        
        elif opcion == "2":
            print("\n--- Buscar Animal ---")
            if not animales:
                print("No hay animales registrados en el sistema.")
                continue
                
            nombre_buscar = input("Ingrese el nombre del animal a buscar: ")
            posicion = buscar_animal(animales, nombre_buscar)
            
            if posicion != -1:
                animal = animales[posicion]
                estado = "EN ALERTA" if animal["alerta"] else "NORMAL"
                print(f"\n¡Animal encontrado en la posición {posicion}!")
                print(f"Nombre: {animal['nombre']} | Especie: {animal['especie']} | Peso: {animal['peso']} kg | Estado: {estado}")
            else:
                print(f"El animal '{nombre_buscar}' no se encuentra registrado.")

       
        elif opcion == "3":
            print("\n--- Eliminar Animal ---")
            if not animales:
                print("No hay animales registrados para eliminar.")
                continue
                
            nombre_eliminar = input("Ingrese el nombre del animal a eliminar: ")
            posicion = buscar_animal(animales, nombre_eliminar)
            
            if posicion != -1:
                animal_eliminado = animales.pop(posicion)
                print(f"El animal '{animal_eliminado['nombre']}' fue eliminado correctamente.")
            else:
                print(f"El animal '{nombre_eliminar}' no se encuentra registrado.")

       
        elif opcion == "4":
            actualizar_alertas(animales)
            print("\n¡Alertas de peso actualizadas para todos los animales!")

       
        elif opcion == "5":
            
            actualizar_alertas(animales)
            
            print("\n=== LISTA DE ANIMALES ===")
            if not animales:
                print("(No hay animales registrados)")
                print("*******************************************")
            else:
                for animal in animales:
                    estado = "EN ALERTA" if animal["alerta"] else "NORMAL"
                    print(f"Nombre: {animal['nombre']}")
                    print(f"Especie: {animal['especie']}")
                    print(f"Peso: {animal['peso']} kg")
                    print(f"Estado: {estado}")
                    print("*******************************************")

        
        elif opcion == "6":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()