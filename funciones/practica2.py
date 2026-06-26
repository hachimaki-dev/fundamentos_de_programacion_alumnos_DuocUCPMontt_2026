sistema_estudiante =[]


def iniciar_programa():
    while True:
        mostrarmenu()
        opcion_usuario = input("Ingrese su opcion: ")
        
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre.strip() == "":
            print("Los datos que ingresa no son validos")
        else:
            return nombre
        
def validar_nota():
    while True:
        try:
            nota = float(input("Ingrese su nota: "))
            if nota < 4.0 or nota > 7.0:
                print("La nota debe ser entre 1.0 y 7.0")
            else:
                return nota
        except ValueError:
             print("Ingrese un numero entero")
    
def agregar_registro():
    nombre_valido = validar_nombre
    asignatura_valida = 


def buscar_registro(registro_buscar):
    for registro_nombre in sistema_estudiante:
        if registro_nombre['Nombre'].lower() == registro_buscar.lower():
            print("Existe")
            return registro_nombre
        else:
            print("No existe")
            return -1
        
def eliminar_registro(registro_buscar):
    indice_registro = buscar_registro(registro_buscar)
    if indice_registro is not None:
        if sistema_estudiante.pop(indice_registro):
            return True
        else:
            print("No se pudo eliminar")
            return False

def actualizar_registro():
    for estudiantes in sistema_estudiante:
        if estudiantes[''] > 0:
            

def mostrarmenu():
    print("1. Agregar registro")
    print("2. Buscar registro")
    print("3. Eliminar registro")
    print("4. Actualizar estados")
    print("5. Mostrar registros")
    print("6. Salir")
    
    
    
    if 
