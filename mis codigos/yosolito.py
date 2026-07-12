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

# ---- indices serie ----
IDX_TITULO = 0
IDX_GENERO = 1
IDX_ESTUDIO = 2
IDX_CLASIFICACION = 3
IDX_SUBTITULADO = 4
IDX_PAIS = 5

# ---- indices catalogo ----
IDX_PRECIO = 0
IDX_EPISODIOS = 1


def buscar_episodios_por_generos(genero_a_buscar):
    genero_a_buscar = genero_a_buscar.lower()
    total_de_episodios = 0
    for id_anime, datos_de_anime in series.items():
        if datos_de_anime[IDX_GENERO].lower == genero_a_buscar.lower():
            total_de_episodios += catalogo[id_anime][IDX_EPISODIOS]
    print(f"los episodios por genero {genero_a_buscar} son de {total_de_episodios}")

def buscar_anime_por_rango_de_precio(precio_minimo,precio_maximo):
    lista_de_animes_encontrados = []
    for id_anime, datos_de_catalogo in catalogo.items():
        precio_actual = [IDX_PRECIO]
        episodios_actuales = [IDX_EPISODIOS]
        