libro = {
    "titulo": "Las cronicas de Martin Cavero",
    "autor": "Martin Cavero",
    "año": 2008
}
print("Titulo", libro["titulo"])
print("Autor", libro["autor"])
print("Año", libro["año"])

libro["año"] = 2026
libro["editorial"] = "Zig-Zag"

print("Titulo", libro["titulo"])
print("Autor", libro["autor"])
print("Año", libro["año"])
print("editorial", libro["editorial"])