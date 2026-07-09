secciones = ["EQ", "ES", "FI"]
laminas_por_seccion = 20
total_laminas =len(secciones) * laminas_por_seccion

def generar_album_completo():
    album ={}
    for seccion in secciones:
        codigos =[]
        for numero in range(1, laminas_por_seccion + 1):
            codigo =f"{seccion}-{numero:02d}"
            codigos.append(codigo)
        album[seccion] = codigos
    return album 

def es_codigo_valido(codigo):
    if len(codigo) != 5:
        return False
    
    seccion = codigo[0:2]
    guion = codigo[2]
    numero_texto = codigo[3:5]
    
    if seccion not in secciones:
        return False
    
    if guion != "-":
        return False
    
    if not numero_texto.isdigit():
        return False
    
    numero = int(numero_texto)
    
    if numero < 1 or numero > laminas_por_seccion:
        return False
    
    return True
    
def buscar_coleccion(lista_coleccion, nombre):
    for i in range(len(lista_coleccion)):
        if lista_coleccion[i]["nombre"].lower() == nombre.lower():
            return i
    return -1

def registrar_coleccionista(lista_coleccion):
    nombre = input("Nombre del coleccionista: ")
    if len(nombre.strip()) == 0:
        print("Error al ingresar nombre")
        return
    nuevo_coleccionista ={
         "nombre": nombre,
           "laminas_pegadas": [],
           "laminas_repetidas": [],
           "porcentaje_avance": 0.0
    }
    
    lista_coleccion.append(nuevo_coleccionista)
    print(f"Coleccionista '{nombre}' registrado con exito")

def calcular_porcentaje(coleccionista):
    cantidad = len(coleccionista["laminas_pegadas"])
    porcentaje = (cantidad / total_laminas) * 100
    return round(porcentaje, 1)

def pegar_lamina(coleccion,codigo):
    if not es_codigo_valido(codigo):
        print("Codigo lamina invalido")
        return
    
    if codigo in coleccion["laminas_pegadas"]:
        print("Esta lamina ya esta pegada. ")
        return
    
    coleccion["laminas_pegadas"].append(codigo)
    coleccion["porcentaje_avance"] = calcular_porcentaje(coleccion)
    print(f"Lámina {codigo} pegada. Avance: {coleccion['porcentaje_avance']}%")
    
def marcar_lamina_repetida(coleccion,codigo):
    if not es_codigo_valido(codigo):
        print("Lamina invalida")
        return
        
    if codigo in coleccion["laminas_pegadas"]:
        print("Esta lamina ya esta pegada. ")
        return
    
    if codigo in coleccion["laminas_repetidas"]:
        print("Esta lamina ya esta marcada como repetida. ")
        return
    
    coleccion["laminas_repetidas"].append(codigo)
    print(f"lamina {codigo} marcada como repetida")
    
def laminas_faltantes(coleccionista):
    album = generar_album_completo()
    faltantes = {}
    
    for seccion in secciones:
        faltantes_seccion = []
        for codigo in album[seccion]:
            if codigo not in coleccionista["laminas_pegadas"]:
                faltantes_seccion.append(codigo)
        faltantes[seccion] = faltantes_seccion
        
    return faltantes


def que_le_falta(receptor, ofertante):
    posible = []
    for codigo in ofertante["laminas_repetidas"]:
        if codigo not in receptor["laminas_pegadas"]:
            posible.append(codigo)
    return posible

coleccionistas = []

def buscar_intercambio(coleccionista_A, coleccionista_B):
    de_a_hacia_b = que_le_falta(coleccionista_B,coleccionista_A)
    de_b_hacia_a = que_le_falta(coleccionista_A, coleccionista_B)
    
    if len(de_a_hacia_b) == 0 and len(de_b_hacia_a) == 0:
        print(f"No hay intercambios posibles entre '{coleccionista_A['nombre']}' y '{coleccionista_B['nombre']}'.")
        return
    if len(de_a_hacia_b) > 0:
        print(f"{coleccionista_A['nombre']} le puede ofrecer a {coleccionista_B['nombre']}: {de_a_hacia_b}")
    
    if len(de_b_hacia_a) > 0:
        print(f"{coleccionista_B['nombre']} le puede ofrecer a {coleccionista_A['nombre']}: {de_b_hacia_a}")


def mostrar_menu():
    print("========== MENÚ ÁLBUM MUNDIAL ==========")
    print("1. Registrar coleccionista")
    print("2. Pegar lámina")
    print("3. Marcar lámina repetidas")
    print("4. Buscar coleccionista")
    print("5. Ver láminas faltantes por secció")
    print("6. Buscar intercambio entre dos coleccionistas")
    print("7. Salir")
    print("==========================================")

def leer_opcion():
    try:
        return int(input("Ingrese su opción: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return None
    
def iniciar_programa():
    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            registrar_coleccionista(coleccionistas)
        
        elif opcion == 2:
                nombre = input("Nombre del coleccionista: ")
                posicion = buscar_coleccion(coleccionistas, nombre)
                if posicion == -1:
                    print("No existe un coleccionista con ese nombre.")
                else:
                    codigo = input("Código de la lámina a pegar: ")
                    pegar_lamina(coleccionistas[posicion], codigo)

        elif opcion == 3:
            nombre = input("Nombre del coleccionista: ")
            posicion = buscar_coleccion(coleccionistas, nombre)
            if posicion == -1:
                print("No existe un coleccionista con ese nombre.")
            else:
                codigo = input("Codigo Lamina duplicada: ")
                marcar_lamina_repetida(coleccionistas[posicion],codigo)
        
        elif opcion == 4:
            nombre = input("Nombre a buscar: ")
            posicion = buscar_coleccion(coleccionistas,nombre)
            if posicion == -1:
                print("No se encontro nigun coleccionista con ese nombre. ")
            else:
                print(coleccionistas[posicion]) 
        
        elif opcion == 5:
            nombre = input("Nombre del coleccionista: ")
            posicion = buscar_coleccion(coleccionistas, nombre)
            if posicion == -1:
                print("No existe un coleccionista con ese nombre.")
            else:
                coleccionista = coleccionistas[posicion]
                faltantes = laminas_faltantes(coleccionista)

                print(f"\n=== AVANCE DE {coleccionista['nombre']} ===")
                print(f"Avance total: {coleccionista['porcentaje_avance']}%\n")
                
                for seccion in secciones:
                    cantida_faltante =len(faltantes[seccion])
                    if cantida_faltante == 0:
                        print(f"Seccion{seccion} - completa")
                    else:
                        print(f"Seccion{seccion} - faltan {cantida_faltante} de {laminas_por_seccion}")
                        print("  " + ", ".join(faltantes[seccion]))
 
            
    
        elif opcion == 6:
            nombre_a = input("Nombre del primer coleccionista: ")
            nombre_b = input("Nombre del segundo coleccionista: ")

            if nombre_a == nombre_b:
                print("Debes ingresar dos coleccionistas distintos.")
            else:
                posicion_a = buscar_coleccion(coleccionistas, nombre_a)
                posicion_b = buscar_coleccion(coleccionistas, nombre_b)   

                if posicion_a == -1 or posicion_b == -1:
                    print("Uno o ambos coleccionistas no existen.")
                else:
                    buscar_intercambio(coleccionistas[posicion_a], coleccionistas[posicion_b])
    
        elif opcion == 7:
            print("Gracias por usar nuestro programa. Hasta luego")   
    
        else:   
            print("Opcion invalida")
    
    
iniciar_programa()

    
   
   
    