lista_de_series_dentro_del_rango=[]

series={
  'AN001': ['Attack on Titan',  'accion', 'MAPPA',   'M', False, 'Japon'],
  'AN002': ['Your Name',     'romance', 'CoMix Wave', 'PG', True, 'Japon'],
  'AN003': ['One Punch Man',   'comedia', 'J.C.Staff', 'PG', False, 'Japon'],
  'AN004': ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],
  'AN005': ['No Game No Life',  'isekai', 'Madhouse', 'PG', True, 'Japon'],
  'AN006': ['Violet Evergarden', 'drama', 'KyoAni',  'G', True, 'Japon'],
}

catalogo={
  'AN001': [9990, 75],
  'AN002': [4990, 0],
  'AN003': [7990, 12],
  'AN004': [8990, 26],
  'AN005': [5990, 13],
  'AN006': [6990, 13]
}

def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Buscar anime por genero.")
    print("2. Buscar anime por precio.")
    print("3. Eliminar registro.")
    print("4. Mostrar registros.") 
    print("5. Salir.")
    print("==========================\n")

def leer_opcion_elegida():
    opcion_elegida = input("Elije una opcion: ")
    if opcion_elegida in ["1", "2", "3", "4", "5"]:
        return opcion_elegida
    else:
        print("Opción no válida.")
        return None

def cantidad_de_episodios_por_genero(genero_a_consultar):
    cantidad_episodios=0
    for cada_serie in series.items():
        if cada_serie[1][1]==genero_a_consultar:
            for cada_serie_en_el_catalogo in catalogo.items():
                if cada_serie_en_el_catalogo[0]==cada_serie[0]:
                    cantidad_episodios+=cada_serie_en_el_catalogo[1][1] 
    return cantidad_episodios

def encontrar_serie_por_rango_de_precio(precio_minimo, precio_maximo):
    for cada_precio in catalogo.items():
        if cada_precio[1][0]>=precio_minimo and cada_precio[1][0]<=precio_maximo:
            for cada_serie in series.items():
                if cada_serie[0]==cada_precio[0]:
                    preparando_los_datos=cada_serie[1][0]+"---"+cada_serie[0]
                    lista_de_series_dentro_del_rango.append(preparando_los_datos)
                    lista_de_series_dentro_del_rango.sort()
    return lista_de_series_dentro_del_rango

def actualizar_precio_por_codigo():
    codigo_user=input("\nIngrese un codigo de articulo: ")
    precio_user=int(input("Ingrese un nuevo precio: "))
    for cada_precio in catalogo.items():
        if codigo_user == cada_precio[0]:
            catalogo[codigo_user][0]=precio_user
            print(catalogo)

def iniciar_programa():
    while True:
        menu_principal()
        opcion = leer_opcion_elegida()
        if opcion == "1":
            cantidad_de_episodios_por_genero()
        elif opcion == "2":
            encontrar_serie_por_rango_de_precio()
        elif opcion == "5":
            break

iniciar_programa()