lista_animales = []

def validar_nombre_animal(nombre):
    if nombre.strip() == "":
        print("Error: El nombre del animal no puede estar vacío.")
        return False
    return True

def validar_especie(especie):
    if especie.strip() == "":
        print("Error: La especie no puede estar vacía.")
        return False
    return True

def validar_peso(peso_str):
    try:
        peso = float(peso_str)
        if peso <= 0:
            print("Error: El peso debe ser un número decimal mayor que cero.")
            return False
        return True
    except ValueError:
        print("Error: Ingrese un peso decimal válido.")
        return False

def registrar_animal(animales):
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie (perro, gato, etc.): ")
    peso_str = input("Ingrese el peso en kilogramos: ")
    
    if validar_nombre_animal(nombre) and validar_especie(especie) and validar_peso(peso_str):
        nuevo_animal = {
            "nombre": nombre.strip(),
            "especie": especie.strip(),
            "peso": float(peso_str),
            "alerta": False  
        }
        animales.append(nuevo_animal)
        print(f"Animal '{nombre.strip()}' registrado correctamente.")
    else:
        print("No se pudo guardar el registro debido a errores de validación.")
        
def buscar_animal(animales, nombre):
    nombre_buscar = nombre.strip().lower()
    for indice, animal in enumerate(animales):
        if animal["nombre"].lower() == nombre_buscar:
            return indice
    return -1

def actualizar_alertas(animales):
    for animal in animales:
        if animal["peso"] < 3.0:
            animal["alerta"] = True
        else:
            animal["alerta"] = False

def mostrar_animales(animales):
    actualizar_alertas(animales)
    print("\n=== LISTA DE ANIMALES ===")
    for animal in animales:
        estado = "EN ALERTA" if animal["alerta"] else "NORMAL"
        print(f"Nombre: {animal['nombre']}")
        print(f"Especie: {animal['especie']}")
        print(f"Peso: {animal['peso']} kg")
        print(f"Estado: {estado}")
        print("*******************************************")


def menu_veterinaria():
    while True:
        print("\n======== Menú Principal ========")
        print("1. Registrar animal")
        print("2. Buscar animal")
        print("3. Eliminar animal")
        print("4. Actualizar alertas")
        print("5. Mostrar animales")
        print("6. Salir")
        print("================================")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            registrar_animal(lista_animales)
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre del animal a buscar: ")
            posicion = buscar_animal(lista_animales, nombre)
            if posicion != -1:
                print(f"El animal fue encontrado en la posición {posicion}.")
            else:
                print(f"El animal '{nombre}' no se encuentra registrado.")
                
        elif opcion == "3":
            nombre = input("Ingrese el nombre del animal a eliminar: ")
            posicion = buscar_animal(lista_animales, nombre)
            if posicion != -1:
                lista_animales.pop(posicion)
                print(f"El animal '{nombre}' ha sido eliminado correctamente.")
            else:
                print(f"El animal '{nombre}' no se encuentra registrado.")
                
        elif opcion == "4":
            actualizar_alertas(lista_animales)
            print("Alertas de peso actualizadas con éxito.")
            
        elif opcion == "5":
            mostrar_animales(lista_animales)
            
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_veterinaria()