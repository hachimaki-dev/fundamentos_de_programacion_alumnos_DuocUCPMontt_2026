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

resultado=encontrar_serie_por_rango_de_precio(5000, 10000)
print(resultado)

def pepito():
    codigo_user=input("\nIngrese un codigo de articulo: ")
    precio_user=int(input("Ingrese un nuevo precio: "))
    for cada_precio in catalogo.items():
        if codigo_user == cada_precio[0]:
            catalogo[codigo_user][0]=precio_user
            print(catalogo)

pepito()