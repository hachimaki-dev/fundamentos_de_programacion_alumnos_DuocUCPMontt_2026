lista = [
    "hola","noob","manco","genial"
]
prohibida = "noob","manco"
for palabra in lista:
    if palabra in prohibida:
        print ("[CENSURADO]")
    else:
        print (palabra)
