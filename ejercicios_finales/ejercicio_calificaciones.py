lista_alumnos = []
def ver_menu():
    print("\n ========== MENÚ PRINCIPAL ==========")
    print("1. Agregar registro")
    print("2. Buscar registro")
    print("3. Eliminar registro")
    print("4. Actualizar estados")
    print("5. Mostrar registros")
    print("6. Salir")
def iniciar_programa():
    while True:
        ver_menu()
        opcion_elegida = opcion()
        if opcion_elegida == 1:
            agregar_registro()
        elif opcion_elegida == 2:
            nombre_del_alumno_buscado = input("ingrese el nombre del alumno que busca: ")
            posicion = buscar_alumno(nombre_del_alumno_buscado)
            if posicion != -1:
                print(f"alumno encontrado en el indice {posicion}")
            else:
                print("no existe")
        elif opcion_elegida == 3:
            nombre_de_alumno_eliminado = input("ingrese el nombre del alumno que desea eliminar: ")
            posicion = buscar_alumno(nombre_de_alumno_eliminado)
            if posicion != -1:
                lista_alumnos.pop(posicion)
                print("alumno eliminado")
        elif opcion_elegida == 4:
            actualizar_aprobados()
            print("los datos han sido actualizados")
        elif opcion_elegida == 5:
            mostrar_alumnos()
        elif opcion_elegida == 6:
            print("adios!!")
            break

def mostrar_alumnos():
    actualizar_aprobados()
    if not lista_alumnos:
        print("la lista esta vacia")
        return
    print("\n === LISTA DE REGISTROS ===")
    for alumno in lista_alumnos:
        print(f"nombre: {alumno['nombre']}")
        print(f"asignatura: {alumno['asignatura']}")
        print(f"nota: {alumno['nota']}")
        if alumno['aprobado']:
            print("este alumno ha aprobado")
        else:
            print("este alumno reprobo")

def alumnos_registrados(diccionario_alumnos):
    lista_alumnos.append(diccionario_alumnos)
    return True

def agregar_registro():
    nombre_alumno = validar_nombre()
    asignatura = validar_asignatura()
    nota_validada = validar_nota()
    print(f"nombre: {nombre_alumno}\nasigantura: {asignatura}\nnota: {nota_validada}")
    datos_del_alumno = {
        'nombre' : nombre_alumno,
        'asignatura' : asignatura,
        'nota'  : nota_validada,
        'aprobado' : False
    }
    alumno_validado = alumnos_registrados(datos_del_alumno)
    return alumno_validado
    
def buscar_alumno(alumno):
    for i, cada_alumno in enumerate(lista_alumnos):
        if cada_alumno['nombre'] == alumno:
            print("el alumno esta registrado")
            return i
    return -1
        
def eliminar_alumno(alumno):
    indice_del_alumno = buscar_alumno(alumno)
    if indice_del_alumno is not None:
        lista_alumnos.pop(indice_del_alumno)
        return True
    
    return False

def actualizar_aprobados():
    for cada_alumno in lista_alumnos:
        if cada_alumno['nota'] >= 4.0:
            print("estado actualizado")
            cada_alumno['aprobado'] = True
        else:
            cada_alumno['aprobado'] = False

def validar_nombre():
    while True:
        nombre_alumno = input("ingrese el nombre del estudiante: ").strip()
        if len(nombre_alumno) <= 0:
            print("nombre invalido, intente nuevamente")
        else:
            return nombre_alumno
        
def validar_asignatura():
    while True:
        nombre_asignatura = input("ingrese el nombre de la asignatura: ").strip()
        if len(nombre_asignatura) <= 0:
            print("nombre invalido, intente nuevamente")
        else:
            return nombre_asignatura
        
def validar_nota():
    while True:
        try:
            nota_alumno = float(input("ingrese la nota del alumno: "))
            if nota_alumno >= 1.0 and nota_alumno <= 7.0 :
                return nota_alumno
            else:
                print("nota invalida")
        except ValueError:
            print("dato invalido, intente nuevamente")

def opcion():
    while True:
        try:
            opcion_elegida = int(input("ingrese una de las opciones del menu: "))
            if opcion_elegida in [1, 2, 3, 4, 5, 6]:
                return opcion_elegida
            else:
                print("opcion invalida, intente nuevamente")
        except ValueError:
            print("ingrese un numero valido por favor")

iniciar_programa()