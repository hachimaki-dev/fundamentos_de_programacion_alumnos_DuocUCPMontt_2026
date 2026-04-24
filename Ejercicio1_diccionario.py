#Muestra cada dato con print().
#Cambia el año por uno más reciente.
#Agrega una nueva clave llamada editorial.



libro = {
    "titulo" : "Dune",
    "autor" : "Frank Herbet",
    "año" : 1964 ,
    "nota" : 4 ,
}

print(libro["titulo"])
print(libro["autor"])
print(libro["año"])

libro["año"] = 1965
libro["editorial"] = "Delbolsillo"

for clave, valor in libro.items():
    print(clave, valor)