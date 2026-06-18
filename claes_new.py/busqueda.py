lista_bichos = [
    {
        "nombre_bicho" : "gusano",
        "longitud" : 9,
        "nivel_peligro": 4.5,
    },
    {
        "nombre_bicho" : "Pulga",
        "longitud" : 2,
        "nivel_peligro": 2.3,
    },
    {
        "nombre_bicho" : "Mariposa",
        "longitud" : 7,
        "nivel_peligro": 1.2,
    },
    {
        "nombre_bicho" : "Escarabajo",
        "longitud" : 12,
        "nivel_peligro": 6.5,
    }
]

bicho_a_buscar = input("Ingrese el nombre del bicho: ")
for cada_bicho in lista_bichos:
    if cada_bicho["nombre_bicho"] == bicho_a_buscar:
        print("")