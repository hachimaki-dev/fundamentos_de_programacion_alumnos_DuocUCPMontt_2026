def validar_nombre(nombre):
    "validar el nombre que no este vacío"
    return len (nombre.strip()) > 0

def validar_asignatura(asignatura):
    "validar que la asignatura no este vacía"
    return len (asignatura.strip()) > 0

def validar_nota(nota):
    "validar que la nota sea un número entre 0 y 100"
    try:
        nota = float(nota)
        if 1.0 <= nota <= 7.0:
            return True
        return False
    except ValueError:
        return False
    

def buscar_registro(lista, nombre_buscar):
    "buscar un registro que coincida con el nombre dado"
    for i in range(len(lista)):
        if lista[i][0].lower() == nombre_buscar.lower():
            return i
    return -1

def actualizar_estados(listas):
    "recorrer la lista y actualizar el estado aprobado según la nota"
    for registro in listas:
        if registro["nota"] >= 4.0:
            registro["aprobado"] = True
        else:
            registro["aprobado"] = False

def main():
    registros = []
    while True:
        print("======MENU PRINCIPAL======")
        print("1. agregar registro")
        print("2. buscar registros")
        print("3. eliminar registro")
        print("4. actualizar estados")
        print("5. mostrar registros")
        print("6. salir")
        opcion = input("Ingrese una opción: ").strip()


        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            if not validar_nombre(nombre):
                print("Error: El nombre no puede estar vacío.")
                continue

            asignatura = input("Ingrese el nombre de la asignatura: ")
            if not validar_asignatura(asignatura):
                print("Error: La asignatura no puede estar vacía.")
                continue

            nota_str = input("Ingrese la nota (1.0 - 7.0): ")
            if not validar_nota(nota_str):
                print("Error: La nota debe ser un número decimal entre 1.0 y 7.0.")
                continue

            
            nuevo_registro = {
                "nombre": nombre.strip(),
                "asignatura": asignatura.strip(),
                "nota": float(nota_str),
                "aprobado": False  
            }
            registros.append(nuevo_registro)
            print("¡Registro agregado con éxito!")

        
        elif opcion == "2":
            if not registros:
                print("El sistema no tiene registros almacenados.")
                continue

            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            posicion = buscar_registro(registros, nombre_buscar)

            if posicion != -1:
                reg = registros[posicion]
                estado_str = "APROBADO" if reg["aprobado"] else "REPROBADO"
                print(f"\nRegistro encontrado en la posición {posicion}:")
                print(f"Nombre: {reg['nombre']} | Asignatura: {reg['asignatura']} | Nota: {reg['nota']} | Estado: {estado_str}")
            else:
                print(f"El estudiante '{nombre_buscar}' no se encuentra en el sistema.")

        
        elif opcion == "3":
            if not registros:
                print("El sistema no tiene registros almacenados.")
                continue

            nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
            posicion = buscar_registro(registros, nombre_eliminar)

            if posicion != -1:
                eliminado = registros.pop(posicion)
                print(f"¡El registro de '{eliminado['nombre']}' fue eliminado exitosamente!")
            else:
                print(f"El registro de '{nombre_eliminar}' no se encuentra en el sistema.")

        
        elif opcion == "4":
            actualizar_estados(registros)
            print("Estados de aprobación actualizados correctamente para todos los alumnos.")

    
        elif opcion == "5":
            if not registros:
                print("No hay registros para mostrar.")
                continue

            # Primero se actualizan los estados de manera obligatoria
            actualizar_estados(registros)

            print("\n=== LISTA DE REGISTROS ===")
            for reg in registros:
                estado_str = "APROBADO" if reg["aprobado"] else "REPROBADO"
                print(f"Nombre: {reg['nombre']}")
                print(f"Asignatura: {reg['asignatura']}")
                print(f"Nota: {reg['nota']:.1f}")
                print(f"Estado: {estado_str}")
                print("*******************************************")

        
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()