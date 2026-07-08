campos_calificaciones = []

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Agregar registro.")
    print("2. Buscar registro.")
    print("3. Eliminar registro.")
    print("4. Mostrar registros.") 
    print("5. Salir.")
   
def leer_opcion_elegida():
    opcion_elegida = input("Elije una opcion: ")
    if opcion_elegida in ["1", "2", "3", "4", "5"]:
        return opcion_elegida
    else:
        print("Opción no válida.")
        return None

def validacion_nota(nota):
    if 1.0 <= nota <= 7.0:
        return True
    else:
        print("Nota no validada. Ingrese una nota entre 1.0 y 7.0.")
        return False
      
def agregar_registro():
    nombre = input("Ingresa nombre: ")
    if not nombre: # Valida que no esté vacío
        print("El nombre no puede estar vacío.")
        return
    asignatura = input("Ingresa asignatura: ")
    try:
        nota = float(input("Ingrese su nota: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    if validacion_nota(nota):
        aprobado = nota >= 4.0
        nuevo_registro = {
            "Nombre": nombre,
            "Asignatura": asignatura,
            "Nota": nota,
            "Aprobado": aprobado
        }
        campos_calificaciones.append(nuevo_registro)
        print("¡Registro agregado con éxito!")

def buscar_registros():
    nombre_buscar = input("Introduce el nombre a buscar: ")
    encontrado = False
    
    for cada_registro in campos_calificaciones:
        if cada_registro["Nombre"].lower() == nombre_buscar.lower():
            print(f"\nEncontrado: {cada_registro}")
            encontrado = True
            
    if not encontrado:
        print("No se encontró ningún registro con ese nombre.")
        
def mostrar_registros():
    if not campos_calificaciones:
        print("No hay registros guardados.")
    for reg in campos_calificaciones:
        print(reg)

def eliminar_registros():
    eliminar_el_registro = input("Indica el registro que quieres elminar: ")
    campos_calificaciones.remove(eliminar_el_registro)
    
def iniciar_programa():
    while True:
        menu_principal()
        opcion = leer_opcion_elegida()
        if opcion == "1":
            agregar_registro()
        elif opcion == "2":
            buscar_registros()
        elif opcion == "3":
            eliminar_registros()
        elif opcion == "4":
            mostrar_registros()
        elif opcion == "5":
            break
        
iniciar_programa()