doxeo={
    "nombre" : "Seba",
    "apellido" : "Huichacura",
    "rut": "20.000.222-K",
    "edad" : 20
}

print (doxeo["nombre"])

pokemon={
    "001" : "Bulbasaur",
    "002" : "Ivysaur",
    "003" : "Venasaur",
    "004" : "Squirtle"
}

for i in pokemon.items():
    print(i[1])