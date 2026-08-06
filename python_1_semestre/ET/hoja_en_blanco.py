series = {
  'AN001': ['Attack on Titan',  'accion', 'MAPPA',   'M', False, 'Japon'],
  'AN002': ['Your Name',     'romance', 'CoMix Wave', 'PG', True, 'Japon'],
  'AN003': ['One Punch Man',   'comedia', 'J.C.Staff', 'PG', False, 'Japon'],
  'AN004': ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],
  'AN005': ['No Game No Life',  'isekai', 'Madhouse', 'PG', True, 'Japon'],
  'AN006': ['Violet Evergarden', 'drama', 'KyoAni',  'G', True, 'Japon'],
}
catalogo = {
  'AN001': [9990, 75],
  'AN002': [4990, 0],
  'AN003': [7990, 12],
  'AN004': [8990, 26],
  'AN005': [5990, 13],
  'AN006': [6990, 13],
}

#para acceder a la clave : 
# diccionario["clave"][valor]
print(catalogo["AN001"][1])#episodios
print(series['AN001'])#a todo el valor de esa clave 
print(series['AN001'][1])# genero del codigo an001
print(series['AN001'][5])# pais del codigo an001


