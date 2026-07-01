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
    'AN006': [6990,  13],
}

def iniciar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("=====================================")

def iniciar_programa():
    while True:
        iniciar_menu()
        opcion_del_usuario = int(input("Ingrese una de las opciones: \n"))
        if opcion_del_usuario == 1:
            genero_del_anime_a_buscar = input("Ingrese el genero del anime: ").lower
            resultado_cantidad_episodios_por_genero = cantidad_episodios_por_genero(genero_del_anime_a_buscar)
            print(resultado_cantidad_episodios_por_genero)
        elif opcion_del_usuario == 2:
            while True:
                try:
                    precio_minimo = int(input("Ingrese el precio minimo: "))
                    precio_maximo = int(input("Ingrese el precio maximo: \n"))
                    busqueda_de_series_por_precio(precio_minimo, precio_maximo)
                    break
                except ValueError:
                    print("Algo fallo")
        elif opcion_del_usuario == 3:
            print
        elif opcion_del_usuario == 4:
            print
        elif opcion_del_usuario == 5:
            print
        elif opcion_del_usuario == 6:
            print
            break

def cantidad_episodios_por_genero(genero):
    acumulador_cantidad_episodios = 0
    for cada_serie in series.items():
        codigo_serie = cada_serie[0]
        if cada_serie[1][1] == genero:
            for cada_item_catalogo in catalogo.items:
                if cada_item_catalogo[0] == codigo_serie:
                    acumulador_cantidad_episodios += cada_item_catalogo
    return acumulador_cantidad_episodios


def busqueda_de_series_por_precio(precio_minimo, precio_maximo):
    resultado_de_busqueda = []
    for serie_posible in catalogo.items():
        precio_posible = serie_posible[1][0]
        if precio_minimo <= precio_posible <= precio_maximo and serie_posible[1][1] > 0:
            resultado_de_busqueda.append(serie_posible)
        else:
            print("Error")
    print("✅")
    print(resultado_de_busqueda)
    return


def actualizar_precio_de_serie():
    while True:
        serie_a_actualizar = input("Ingrese la ID de la serie: \n")
        if serie_a_actualizar in catalogo:
            actualizar_precio = int(input("Ingrese el nuevo valor de la serie: \n"))
            catalogo[serie_a_actualizar] = actualizar_precio
        else:
            print("La serie que buscas no existe")
        print("¿Desea actualizar otro precio?")
        print("1) Si")
        print("2) No")
        volver_a_actualizar = input("")
        if volver_a_actualizar == 1 or volver_a_actualizar == "Si":

        else:



iniciar_programa()