series = {
    'AN001': ['Attack on Titan',    'accion',  'MAPPA',      'M',  False, 'Japon'],
    'AN002': ['Your Name',          'romance', 'CoMix Wave', 'PG', True,  'Japon'],
    'AN003': ['One Punch Man',      'comedia', 'J.C.Staff',  'PG', False, 'Japon'],
    'AN004': ['Kimetsu no Yaiba',   'accion',  'ufotable',   'PG', True,  'Japon'],
    'AN005': ['No Game No Life',    'isekai',  'Madhouse',   'PG', True,  'Japon'],
    'AN006': ['Violet Evergarden',  'drama',   'KyoAni',     'G',  True,  'Japon'],
}
catalogo = {
    'AN001': [9990,  75],
    'AN002': [4990,   0],
    'AN003': [7990,  12],
    'AN004': [8990,  26],
    'AN005': [5990,  13],
    'AN006': [6990,  13],}

def mostrar_menu():
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("7. Insertar diccionario")

def validar_opciones_del_usuario():
    opcion_usuario_ingresada = input("Ingrese una opcion: ")
    if opcion_usuario_ingresada in ["1","2","3","4","5","6","7"]:
        return opcion_usuario_ingresada
    else:
        print("Debe seleccionar una opción válida")

def validar_titulo():
    titulo = input("Ingrese titulo: ")
    if titulo <= 0 or titulo.isspace():
        print("Titulo no valido")
    else:
        return titulo

def validar_genero():
    genero = input("Ingrese genero: ")
    if genero <= 0 or genero.isspace():
        print("Genero no valido")
    else:
        return genero

def validar_estudio():
    estudio = input("Ingrese estudio: ")
    if estudio <= 0 or estudio.isspace():
        print("Estudio no valido")
    else:
        return estudio

def validar_clasificacion():
    clasificacion = input("Ingrese clasificacion: ")
    if clasificacion in ["G", "PG", "M"]:
        return clasificacion
    else:
        print("Clasificacion no valida")

def validar_subtitulo():
    subtitulo = input("¿Esta subtitulado?, (S = si, N = No) : ")
    if subtitulo in ["S", "N"]:
        return subtitulo
    else:
        print("Subtitulado no es valido")

def validar_pais_origen():
    pais_origen = input("Ingrese pais de origen: ")
    if pais_origen <= 0 or pais_origen.isspace():
        print("Pais de origen invalido")
    else:
        return pais_origen

def cantidad_de_episodios_por_genero(parametro_genero):
    for cada_anime in series.items():
        if cada_anime[1][1] == parametro_genero:

            
def validar_precio():

def validar_episodios():
