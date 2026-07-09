registros_alumnos = []

def validar_nombre(nombre):
    if nombre.strip() == "":
        print("Error: El nombre del estudiante no puede estar vacío.")
        return False
    return True

def validar_asignatura(asignatura):
    if asignatura.strip() == "":
        print("Error: La asignatura no puede estar vacía.")
        return False
    return True

def validar_nota(nota_str):
    try:
        nota = float(nota_str)
        if nota < 1.0 or nota > 7.0:
            print("Error: La nota debe ser un número decimal entre 1.0 y 7.0 inclusive.")
            return False
        return True
    except ValueError:
        print("Error: Ingrese una calificación decimal válida.")
        return False

def agregar_registro(registros):
    nombre = input("Ingrese el nombre del estudiante: ")
    asignatura = input("Ingrese la asignatura: ")
    nota_str = input("Ingrese la nota (1.0 a 7.0): ")
    
    if validar_nombre(nombre) and validar_asignatura(asignatura) and validar_nota(nota_str):
        nuevo_registro = {
            "nombre": nombre.strip(),
            "asignatura": asignatura.strip(),
            "nota": float(nota_str),
            "aprobado": False 
        }
        registros.append(nuevo_registro)
        print(f"Registro de '{nombre.strip()}' agregado correctamente.")
    else:
        print("No se pudo guardar el registro debido a errores de validación.")

def buscar_registro(registros, nombre):
    nombre_buscar = nombre.strip().lower()
    for indice, reg in enumerate(registros):
        if reg["nombre"].lower() == nombre_buscar:
            return indice
    return -1


def actualizar_estados(registros):
    for reg in registros:
        if reg["nota"] >= 4.0:
            reg["aprobado"] = True
        else:
            reg["aprobado"] = False

def mostrar_registros(registros):
    actualizar_estados(registros)
    print("\n=== LISTA DE REGISTROS ===")
    for reg in registros:
        estado = "APROBADO" if reg["aprobado"] else "REPROBADO"
        print(f"Nombre: {reg['nombre']}")
        print(f"Asignatura: {reg['asignatura']}")
        print(f"Nota: {reg['nota']}")
        print(f"Estado: {estado}")
        print("*******************************************")


def menu_calificaciones():
    while True:
        print("\n======== Menú Principal ========")
        print("1. Agregar registro")
        print("2. Buscar registro")
        print("3. Eliminar registro")
        print("4. Actualizar estados")
        print("5. Mostrar registros")
        print("6. Salir")
        print("================================")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            agregar_registro(registros_alumnos)
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            posicion = buscar_registro(registros_alumnos, nombre)
            if posicion != -1:
                print(f"El registro fue encontrado en la posición {posicion}.")
            else:
                print(f"El registro de '{nombre}' no se encuentra en el sistema.")
                
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante a eliminar: ")
            posicion = buscar_registro(registros_alumnos, nombre)
            if posicion != -1:
                registros_alumnos.pop(posicion)
                print(f"El registro de '{nombre}' ha sido eliminado correctamente.")
            else:
                print(f"El registro de '{nombre}' no se encuentra en el sistema.")
                
        elif opcion == "4":
            actualizar_estados(registros_alumnos)
            print("Estados de aprobación actualizados con éxito.")
            
        elif opcion == "5":
            mostrar_registros(registros_alumnos)
            
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
menu_calificaciones()

