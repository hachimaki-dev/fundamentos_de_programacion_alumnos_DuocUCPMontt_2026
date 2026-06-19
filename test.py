lista_de_todos_los_bichos = [
    {
        "especie_bicho": "chinita",
        "longitud_bicho": 2,
        "peligrosidad_bicho": 3.1,
        "es_peligroso": False
    },
    {
        "especie_bicho": "palote",
        "longitud_bicho": 8,
        "peligrosidad_bicho": 4.5,
        "es_peligroso": False
    },
    {
        "especie_bicho": "chanchito",
        "longitud_bicho": 3,
        "peligrosidad_bicho": 1.3,
        "es_peligroso": False
    }

]

def buscar_nombre_del_bicho(nombre_del_bicho_a_buscar):
    for cada_bicho in lista_de_todos_los_bichos:
        if cada_bicho["especie_bicho"] == nombre_del_bicho_a_buscar:
            indice_de_bicho = lista_de_todos_los_bichos.index(cada_bicho)
            return indice_de_bicho
        elif cada_bicho["especie_bicho"] != nombre_del_bicho_a_buscar and lista_de_todos_los_bichos.index(cada_bicho) < 2:
            continue

def eliminar_bicho(indice_de_bicho):
    return lista_de_todos_los_bichos.pop(indice_de_bicho)

buscar_nombre_del_bicho("palote")
eliminar_bicho(indice_de_bicho)

print(lista_de_todos_los_bichos)