libro = {
    "titulo":"Harry Potter",
    "autor":"J.K ROlling",
    "año":1998
}

libro["año"]=2000
libro["editorial"]="salamandra"

for clave, valor in libro.items():
    print(clave,valor)