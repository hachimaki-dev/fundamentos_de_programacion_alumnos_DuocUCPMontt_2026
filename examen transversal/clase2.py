series = {

  'AN001': ['Attack on Titan',  'accion', 'MAPPA',   'M', False, 'Japon'],

  'AN002': ['Your Name',     'romance', 'CoMix Wave', 'PG', True, 'Japon'],

  'AN003': ['One Punch Man',   'comedia', 'J.C.Staff', 'PG', False, 'Japon'],

  'AN004': ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],

  'AN005': ['No Game No Life',  'isekai', 'Madhouse', 'PG', True, 'Japon'],

  'AN006': ['Violet Evergarden', 'drama', 'KyoAni',  'G', True, 'Japon'],

  'AN007': ['Spirited Away',   'fantasia', 'Ghibli',  'G', True, 'Japon'],

  'AN008': ['Fullmetal Alchemist','accion', 'Bones',   'PG', False, 'Japon'],

  'AN009': ['Death Note',    'suspenso', 'Madhouse', 'M', False, 'Japon'],

  'AN010': ['Jujutsu Kaisen',  'accion', 'MAPPA',   'M', True, 'Japon'],

  'AN011': ['Kaguya-sama',    'comedia', 'A-1 Pictures', 'PG', True, 'Japon'],

  'AN012': ['Chainsaw Man',   'accion', 'MAPPA',   'M', False, 'Japon'],

  'AN013': ['Sousou no Frieren', 'fantasia', 'Madhouse', 'PG', False, 'Japon']

}



catalogo = {

  'AN001': [9990, 75],

  'AN002': [4990, 0],

  'AN003': [7990, 12],

  'AN004': [8990, 26],

  'AN005': [5990, 13],

  'AN006': [6990, 13],

  'AN007': [4500, 5], # Spirited Away

  'AN008': [9500, 64], # Fullmetal Alchemist

  'AN009': [8500, 37], # Death Note

  'AN010': [8990, 24], # Jujutsu Kaisen

  'AN011': [7500, 36], # Kaguya-sama

  'AN012': [8990, 12], # Chainsaw Man

  'AN013': [9990, 28] # Sousou no Frieren

}





def contar_capitulos_por_genero(el_genero_a_contar):

  #Accion

  #Romance

  acumulador_cantidad_episodios = 0

  for cada_serie in series.items() :

    #Si acaso este genero es igual al que recibo por parametro (al que ando buscando)

    if cada_serie[1][1] == el_genero_a_contar :

      for cada_anime_en_catalogo in catalogo.items():

        if cada_anime_en_catalogo[0] == cada_serie[0]:

          acumulador_cantidad_episodios += cada_anime_en_catalogo[1][1]

  return acumulador_cantidad_episodios
def buscador_de_serie_por_rango_de_precio(minimo,maximo):
    for por_cada_catalogo in catalogo.items():
      if por_cada_catalogo[1][0] >= minimo and por_cada_catalogo[1][0] <= maximo:
        