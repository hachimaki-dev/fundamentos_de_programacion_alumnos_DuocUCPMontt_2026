lista_de_bichos = [
    {
        "nombre_especie" : "mariposa",
        "tamaño_bicho" : 3,
        "peligrosidad_bicho" : 2.2,
        "es_peligroso" : False
    },
    {
        "nombre_especie" : "gusano",
        "tamaño_bicho" : 2,
        "peligrosidad_bicho" : 2.9,
        "es_peligroso" : False
    },
    {
        "nombre_especie" : "pulga",
        "tamaño_bicho" : 1,
        "peligrosidad_bicho" : 1.1,
        "es_peligroso" : False
    }
    
]

especie_a_buscar = input("Que bicho estas buscando: ")
for cada_bicho in lista_de_bichos:
    if cada_bicho("nombre_especie") == especie_a_buscar:
        print("")
        break