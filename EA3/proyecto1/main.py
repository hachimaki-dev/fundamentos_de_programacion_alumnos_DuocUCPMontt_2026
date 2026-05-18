from helloworld import HelloWorld
protagonista = {
    "nombre": "Hernan Carcamoo",
    "hp": 100,
    "ataque": 6,
    "magia": 100,
    "ataques_Magicos": [
        {
        "nombre_ataque_magico": "bola de fuego",
        "potencia" : 60
        },
        {
        "nombre_ataque_magico": "cono de hielo",
        "potencia" : 100
        },
        {
        "nombre_ataque_magico" : "POWER WORD KILL",
        "potencia" : 999999
        }
    ]
}

monstruo = {
    "nombre" : "wiwiwi",
    "hp": 30,
    "ataque": 7
}

def combate(datos_protagonista, datos_monstruo):
    datos_protagonista["hp"] = datos_protagonista["hp"] - datos_monstruo["ataque"]
    datos_monstruo["hp"] = datos_monstruo["hp"] - datos_protagonista["ataque"]
    print(f"la vida luego del ataque es: {datos_protagonista["hp"]}")
    print(f"la vida de {datos_monstruo["nombre"]} es {datos_monstruo["hp"]}")
while protagonista["hp"] > 0 and monstruo["hp"] > 0:
    combate(protagonista, monstruo)
HelloWorld("wawa")