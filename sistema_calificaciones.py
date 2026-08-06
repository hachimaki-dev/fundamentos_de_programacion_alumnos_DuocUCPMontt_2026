lista_alumnos = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar registro")
    print("2. Buscar registro")
    print("3. Eliminar registro")
    print("4. Actualizar estados")
    print("5. Mostrar registros")
    print("6. Salir")
    print("=====================================\n")
      
    
def validar_nota():
    while True:
        try:   
            nota_alumno = float(input("Ingresa la nota del estudiante: "))
        except ValueError:
            print("Ingresa un valor valido.")

        if nota_alumno <= 0 or nota_alumno > 7.0:
            print("Ingrese una nota valida en un rango del 1 al 7!")
        else:
            print("Nota valida!")
            return nota_alumno
    
def agregar_registro():
    nombre_alumno = input("Ingresa el nombre del estudiante: ")
    asignatura_alumno = input("Ingresa el nombre de la asignatura: ")
    nota_validada = validar_nota()
    
    
    datos_alumnos = {
        "nombre_alumno" : nombre_alumno ,
        "asignatura_alumno" : asignatura_alumno ,
        "nota_alumno" : nota_validada ,
        "estado" : False
    }

    lista_alumnos.append(datos_alumnos)
    

def buscar_alumno():
    alumno_buscado = input("Ingrese el nombre del alumno que busca: ")

    for alumno in lista_alumnos:
        if alumno["nombre_alumno"] == alumno_buscado:
            print(f"El alumno {alumno["nombre_alumno"]} ha sido encontrado!")
            return alumno
    return None

def actualizar_estado():
    for alumno in lista_alumnos:
        print(f"Se comprobo el registro del alumno {alumno["nombre_alumno"]}")
        if alumno["nota_alumno"] >= 4:
            alumno["estado"] = True
        else:
            alumno["estado"] = False
             

def eleccion_menu_usuario():
    while True:
        try:
            opcion_elegida = int(input("Ingresa tu elección: "))
            
            if opcion_elegida in [1, 2, 3, 4, 5, 6]:
                return opcion_elegida
            else:
                print("Ingresa una de las 6 opciones disponibles.")
        except ValueError:
            print("Ingresa un valor valido.")
            
def mostrar_registros():
    for alumno in lista_alumnos:
        print(f"Nombre: {alumno["nombre_alumno"]}")
        print(f"Asignatura: {alumno["asignatura_alumno"]}")
        print(f"Nota: {alumno["nota_alumno"]}")
        print(f"Estado: {alumno["estado"]}")

def eliminar_alumno():
    alumno_eliminado = buscar_alumno()
    if alumno_eliminado == None:
        print("No hay ningun registro de ese alumno")
    else:
        print("Se eliminara al alumno")
        lista_alumnos.remove(alumno_eliminado)

def main():
    while True:
        mostrar_menu()

        opcion_elegida = eleccion_menu_usuario()
        
        if opcion_elegida == 1:
            agregar_registro()

        elif opcion_elegida == 2:
            buscar_alumno()

        elif opcion_elegida == 3:
            eliminar_alumno()

        elif opcion_elegida == 4:
            actualizar_estado()
        
        elif opcion_elegida == 5:
            mostrar_registros()
            
        elif opcion_elegida == 6:
            print("=== HASTA PRONTO! ===")
            break

main()