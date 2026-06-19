lista_De_bichos = [
    {
        "nombre_especie" : 'Mariposa',
        "longitud_especie" : 8,
        "peligrosidad_especie" : 2.9,
        "es_peligroso" : False
    }
    {
        "nombre_especie" : 'gusano',
        "longitud_especie" : 8,
        "peligrosidad_especie" : 2.9,
        "es_peligroso" : False
    }
    {
        "nombre_especie" : 'pulga',
        "longitud_especie" : 8,
        "peligrosidad_especie" : 2.9,
        "es_peligroso" : False
    }
]    

especie_a_buscar = input('Que especie desea buscar')
for cada_bichos in lista_De_bichos:
    if cada_bichos[nombre_especie] == especie_a_buscar:
