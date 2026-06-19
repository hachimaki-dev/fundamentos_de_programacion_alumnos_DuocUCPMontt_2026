

# def saludar(nombre):
#     print(f"hola {nombre} como estas")
#     return "chao"


# respuesta = saludar("messi")

# print(f"{respuesta}")


prota ={
    "nombre": "hernan mano quemada",
    "hp": 100,
    "ataque": 25,
    "magia": 100,
    "ataques_magicos": [
        {
            "nombre_ataque_magico": "bola de fuego",
            "potencia": 50
        },
        {
            "nombre_ataque_magico": "lluvia magica",
            "potencia": 60
        },
        {
            "nombre_ataque_magico": "canto mortal",
            "potencia": 99999
        },
    ]
}


monstruo = {
    "nombre": "Eltermo",
    "hp" : 30,
    "ataque": 99
}

def combate(datos_prota, datos_monstruo):
    #monstruo ataca primero
    datos_prota["hp"] = datos_prota["hp"] - datos_monstruo["ataque"]

    print(f"la vida luego del ataque es: {datos_prota["hp"]}")

    datos_monstruo["hp"] = datos_monstruo["hp"] - datos_prota["ataque"]

    print(f"la vida luego del ataque es: {datos_monstruo["hp"]}")

combate(prota, monstruo)




