animes_filtrados_por_rango_de_precio = []
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
#serie
IDX_TITULO = 0
IDX_GENERO = 1
IDX_ESTUDIO = 2
IDX_CLASIFICACION = 3
IDX_SUBTITULADO = 4
IDX_PAIS = 5
#catalogo
IDX_PRECIO = 0
IDX_EPISODIOS = 1

def contar_capitulos_por_genero(genero_a_buscar):
    total_de_episodios_por_genero = 0
    for cada_serie in series.items():
        if cada_serie[1][1] == genero_a_buscar:
            for cada_serie_en_el_catalogo in catalogo.items():
                if cada_serie_en_el_catalogo[0] == cada_serie[0]:
                    total_de_episodios_por_genero += cada_serie_en_el_catalogo[1][1]
    return total_de_episodios_por_genero    
    
    
def BusquedaPorPrecio(precio_minimo,precio_maximo):
    for cada_precio_del_catalogo in catalogo.items():
        if cada_precio_del_catalogo[1][0] >= precio_minimo and cada_precio_del_catalogo[1][0] <= precio_maximo:
            id_anime = cada_precio_del_catalogo[0]
            for cada_serie in series.items():
                if id_anime == cada_serie[0]:
                    print(f"el anime es {cada_serie[1][0]}")
                    diccionario_temporal_animes ={
                        "id_anime": cada_serie[0],
                        "nombre_anime" : cada_serie[1][0],
                        "precio_anime" : cada_precio_del_catalogo[1][0]
                    }
                    animes_filtrados_por_rango_de_precio.append(diccionario_temporal_animes)
    return animes_filtrados_por_rango_de_precio