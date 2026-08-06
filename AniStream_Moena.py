series = {
    'AN001' : ['Attack on titan', 'accion', 'MAPPA', 'M', False, 'Japon'],
    'AN002' : ['Your name', 'romance', 'CoMix Wave', 'PG', True, 'Japon'],
    'AN003' : ['One Punch Man', 'comedia', 'J.C.Staff', 'PG', False, 'Japon'],
    'AN004' : ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],
    'AN005': ['No Game No Life',    'isekai',  'Madhouse',   'PG', True,  'Japon'],
    'AN006': ['Violet Evergarden',  'drama',   'KyoAni',     'G',  True,  'Japon']
}

catalogo = {
    'AN001': [9990,  75],
    'AN002': [4990,   0],
    'AN003': [7990,  12],
    'AN004': [8990,  26],
    'AN005': [5990,  13],
    'AN006': [6990,  13],
}

def validar_texto(texto):
    return len(texto.strip()) > 0

def validar_clasificacion(c):
    return c in ['G', 'PG', 'M']

def mostrar_menu():
    print("=== MENU ===\n")
    print("1.- Episodios por genero")
    print("2.- Busqueda de series por rango de precio")
    print("3.- Actualizar precio de serie")
    print("4.- Agregar serie")
    print("5.- Eliminar serie")
    print("6.- Salir")

def opcion_usuario():
    while True:
        try:
            opcion_usuario = int(input("Seleccione una opcion del menú: "))
            if opcion_usuario not in [1, 2, 3, 4, 5, 6]:
                print("Ingresa una opcion valida")
                return None
            else:
                return opcion_usuario
        except ValueError:
            print("ERROR, ingresa un tipo de dato valido")
            return None

def busqueda_precios(precio_minimo, precio_maximo):
    resultados = []

    for id_serie in catalogo:
        precio = catalogo[id_serie][0]
        episodios = catalogo[id_serie][1]

        if precio_minimo <= precio <= precio_maximo and episodios > 0:
            titulo = series[id_serie][0]
            resultados.append(f"{titulo}-{id_serie}")

    if len(resultados) == 0:
        print("No hay resultados")
    else:
        resultados.sort()
        for resultado in resultados:
            print(resultado)

def episodios_por_genero():
    total_episodios = 0
    encontrado = False
    nombre_genero = input("Ingresa el nombre del género que buscas: ").lower().strip()
    if not validar_texto(nombre_genero):
        print("Genero invalido")
        return None

    for serie in series.items():
        if nombre_genero == serie[1][1]: #indice 1 = genero
            encontrado = True
            id_serie = serie[0]
            
            total_episodios += catalogo[id_serie][1]

    if encontrado == True:
        print(f"Hay {total_episodios} episodios de {nombre_genero}")
    
    else:
        print("No se ha encontrado ninguna serie de ese genero")


    while True:
        try:
            precio_maximo = int(input("Ingrese el precio maximo de busqueda: "))
            if precio_maximo < 0:
                print("Ingrese un precio valido!")
                continue
            
            print("Precio maximo registrado")
            return precio_maximo
        except ValueError:
            print("ERROR, ingrese un tipo de dato valido")

def actualizar_precios(id_serie, nuevo_precio):
    id_serie = id_serie.upper().strip()

    if id_serie in catalogo:
        catalogo[id_serie][0] = nuevo_precio
        return True

    return False

def agregar_serie(id_serie, titulo, genero, estudio, clasificacion, subtitulo, pais, precio, episodios):
    id_serie = id_serie.upper().strip()

    if id_serie in series:
        return None
    
    if not all([
        validar_texto(titulo),
        validar_texto(genero),
        validar_texto(estudio),
        validar_clasificacion(clasificacion),
        validar_texto(pais)
    ]):
        return None
    
    subtitulos = subtitulo.lower().strip() == "s"
    series[id_serie] = [titulo, genero, estudio, clasificacion, subtitulo, pais]
    catalogo[id_serie] = [precio, episodios]
    return True


def eliminar_serie(id_serie):
    id_serie = id_serie.upper()

    if id_serie in series:
        del series[id_serie]
        del catalogo[id_serie]
        return True
    return False

def main():
    while True:
        mostrar_menu()

        eleccion_usuario = opcion_usuario()
        
        if eleccion_usuario == 1:
            episodios_por_genero()
        
        elif eleccion_usuario == 2:
            try:
                precio_minimo = int(input("Ingrese el precio minimo: "))
                precio_maximo = int(input("Ingrese el precio maximo: "))
                busqueda_precios(precio_minimo, precio_maximo)
            except ValueError:
                print("ERROR, ingrese un dato valido")
        
        elif eleccion_usuario == 3:
            id_serie = input("Ingrese el id de la serie a la que se le actualizara el precio: ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                if actualizar_precios(id_serie, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("No existe el codigo")
            except ValueError:
                print("ERROR, ingrese un dato valido")
        
        elif eleccion_usuario == 4:
            id_serie = input("Ingrese el ID de la serie que desea añadir: ")
            titulo = input("Ingrese el nombre de la serie a agregar: ")
            genero = input("Ingrese el nombre del genero: ")
            estudio = input("Ingrese el nombre del estudio: ")
            clasificacion = input("Ingrese la clasificacion de la serie (G/PG/M): ")
            subtitulos = input("Esta subtitulado?(s/n): ")
            pais = input("Ingrese el pais de la serie: ")
            precio = int(input("Ingrese el precio de la serie"))
            episodios = int(input("Ingrese la cantidad de episodios: "))

            if agregar_serie(id_serie, titulo, genero, estudio, clasificacion, subtitulos, pais, precio, episodios):
                print("Serie agregada")
            
            else:
                print("ERROR al agregar la serie")

        elif eleccion_usuario == 5:
            id_serie = input("Ingrese el ID de la serie a eliminar: ")
            if eliminar_serie(id_serie):
                print("Serie eliminada")
            
            else:
                print("ERROR al eliminar serie")

        elif eleccion_usuario == 6:
            print("Hasta pronto!")
            break

main()