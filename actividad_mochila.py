
estado_mochila=False

mochila_real={
    "bolsillo":{"manga":"One Pice",
                "libro":"Dune",
                "Mouse":"blanco"}
}

mochila_fake={
    "bolsillo":{"manga":"Boku no Hero",
                "libro":"Twilight",
                "Mouse":"negro"},
}

estado_mochila=input("Desea abrir la mochila?\n")
if estado_mochila=="SI":
    estado_mochila=True
if estado_mochila==True:
    print(mochila_real)

if len(mochila_real):
    print(len(mochila_real["bolsillo"]))
for cosa, descripcion in mochila_real["bolsillo"].items:
    print(descripcion)