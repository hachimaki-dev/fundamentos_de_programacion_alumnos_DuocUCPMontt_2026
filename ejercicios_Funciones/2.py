lista_calificaciones = []

def mostrar_menu():
    print("1. Agregar registro")
    print("2. Buscar registro")
    print("3. Eliminar registro")
    print("4. Actualizar estados")
    print("5. Mostrar registros")
    print("6. Salir")
    print("7. Insertar lista")
def leer_opcion():
    while True:
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada in ["1","2","3","4","5","6","7"]:
            return opcion_ingresada
        else:
            print("Opcion invalida, vuelva a intentarlo")
def validar_nombre(nombre):
    nombre_validado = nombre.strip()
    if nombre_validado != " ":
        return True
    else:
        return False
def validar_asignatura(asignatura):
    asignatura_validado = asignatura.strip()
    if asignatura_validado != " ":
        return True
    else:
        return False
def validar_nota(nota):
    try:
        nota = float(nota)
        if 1.0 <= nota <= 7.0:
            return True
        else:
            return False
    except ValueError:
        return False
def agregar_registro():
    nombre = input("Ingrese nombre: ")
    if not validar_nombre(nombre):
        print("Error: Ingrese un nombre valido")
        return
    asignatura = input("Ingrese asignatura: ")
    if not validar_asignatura(asignatura):
        print("Error: Ingrese una asignatura valida")
        return
    nota = input("Ingrese nota: ")
    if not validar_nota(nota):
        print("Error: Ingrese una nota valida")
    
    calificaciones = {
        "nombre": nombre,
        "asignatura": asignatura,
        "nota": nota,
        "estado": False
    }
    lista_calificaciones.append(calificaciones)
    print("Datos registrados.")
def buscar_registro(nombre_buscar_estudiante):
    buscar = nombre_buscar_estudiante.lower().strip()
    for i in range(len(lista_calificaciones)):
        if lista_calificaciones[i]["nombre"].lower() == buscar:
            return i
    return -1
def eliminar_registro(nombre_buscar_estudiante):
    eliminar = input("Ingrese nombre a eliminar: ")
    indice = nombre_buscar_estudiante(lista_calificaciones, eliminar)
    if indice != -1:
        eliminando = lista_calificaciones.pop(indice)
        print(f"Se elimino {eliminando["nombre"]}")
    else:
        print(f"Error: El registro de {eliminando["nombre"]} no se encuentra")
def actualizar_estado():
    for calificaciones in lista_calificaciones:
        if calificaciones["nota"] >= 4.0:
            calificaciones["estado"] = "aprobado"
        else:
            calificaciones["estado"] = "reprobado"
    print("Datos actualizados")
def insertar_lista():
    lista_calificaciones.append({
        "nombre": "Ana Pérez",
        "asignatura": "Matemáticas",
        "nota": 5.5,
        "estado": "aprobado"
    })
    lista_calificaciones.append({
        "nombre": "Luis Mora",
        "asignatura": "Historia",
        "nota": 3.2,
        "estado": "reprobado"
    })
def mostrar_registro():
    if len(lista_calificaciones) == 0:
        print("No hay nada que mostrar")
        return
    else:
        print(lista_calificaciones)

def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == "1":
            agregar_registro()
        elif opcion == "2":
            registro_buscar = input("Ingrese nombre a buscar: ")
            indice_encontrado = buscar_registro(registro_buscar)
            if indice_encontrado is not None:
                print("Lo encontramos")
                print(f"Con nombre {lista_calificaciones[indice_encontrado]["nombre"]}")
                print(f"Con la asignatura {lista_calificaciones[indice_encontrado]["asignatura"]}")
                print(f"Con la nota {lista_calificaciones[indice_encontrado]["nota"]}")
                print(f"Con el estado de {lista_calificaciones[indice_encontrado]["estado"]}")
            else:
                print("No se encontro nada.")
        elif opcion == "3":
            eliminar_registro()
        elif opcion == "4":
            actualizar_estado()
        elif opcion == "5":
            mostrar_registro()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        elif opcion == "7":
            insertar_lista()
          
main()
