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

print("\n========== MENÚ PRINCIPAL ==========")
print("1. Episodios por género")
print("2. Búsqueda de series por rango de precio")
print("3. Actualizar precio de serie")
print("4. Agregar serie")
print("5. Eliminar serie")
print("6. Salir")
print("=====================================\n")

#while True:
#    opcion_usuario=input("Por favor ingrese una opcion")
#    if opcion_usuario==1:
#        genero=input("Por favor ingrese el nombre de un genero")
#    elif opcion_usuario==2:
#        rango_de_precio=int(input("Por favor ingrese un rango de precio"))
#   elif opcion_usuario==3:
#    elif opcion_usuario==4:
#    elif opcion_usuario==5:
#   elif opcion_usuario==6:
#        print("\nSaliendo...\n")
#        break
#    else:
#        print("\nOpcion invalida, porfavor eliga una de las opciones.\n")

def cant_ep_genero(genero_a_consultar):
    for cada_serie in series.items():
        if cada_serie[1][1]==genero_a_consultar:
            for cada_serie_en_el_catalogo in catalogo.items():
                if cada_serie_en_el_catalogo[0]==cada_serie[0]:
                    print(cada_serie_en_el_catalogo[1][1])
cant_ep_genero("accion")

def series_por_precio(precio_min, precio_max):
    for cada_serie in series.items():
        if cada_serie[1][0]>=precio_min and cada_serie[1][0]<=precio_max:
            for cada_serie_en_el_catalogo in catalogo.items():
                if cada_serie_en_el_catalogo[0]==cada_serie[0]:
                    print(cada_serie_en_el_catalogo[1][1])
series_por_precio(5000, 8000)