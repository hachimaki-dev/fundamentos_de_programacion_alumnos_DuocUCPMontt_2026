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

def contar_episodios_por_genero(genero_a_buscar):
    genero_a_buscar = genero_a_buscar.lower()
    total_de_episodios_por_genero = 0
    for codigo_serie, datos_de_anime in series.items():
        if datos_de_anime[IDX_GENERO].lower() == genero_a_buscar:
            total_de_episodios_por_genero += catalogo[codigo_serie][IDX_EPISODIOS]
    print(f"los capitulos que hay para{genero_a_buscar} son de {total_de_episodios_por_genero} episodios")

def buscar_series_por_rango_de_precio(precio_minimo,precio_maximo):
    lista_de_series_encontradas = []
    for codigo_serie,datos_de_anime in catalogo.items():
        
        precio_actual = datos_de_anime[IDX_PRECIO]
        episodios_actuales = datos_de_anime[IDX_EPISODIOS]
        
        precio_dentro_del_rango = precio_minimo<=  precio_actual <= precio_maximo
        tiene_episodios_disponibles = episodios_actuales > 0
        
        if precio_dentro_del_rango and tiene_episodios_disponibles:
            titulo_serie = series[codigo_serie][IDX_TITULO]
            lista_de_series_encontradas.append(f"{titulo_serie}--{codigo_serie} ")
    
    if len(lista_de_series_encontradas) == 0:
        print("no se encontraron series con ese rango de precio.")
        return
    lista_de_series_encontradas.sort()
    for linea in lista_de_series_encontradas:
        print(linea)

 
def actualizar_precio_de_serie(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in catalogo:
        catalogo[codigo][IDX_PRECIO] == nuevo_precio
        return True
    return False

def validar_texto_no_vacio(texto):
    return texto.strip() != "" 

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ("G","PG","M")










def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Episodios por genero")
    print("2. Busqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("=====================================")
  



