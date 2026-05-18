protagonista = {
    "nombre"    : "Hernan Manoquemada",
    "hp"        : 100,
    "ataque"    : 6,
    "magia"     : 100,
    "ataques_magicos"   : [
        {
            "nombre_ataque_magico" : "Bola de Fuego",
            "potencia" : 10
        },
         {
            "nombre_ataque_magico" : "Luvia mágica",
            "potencia" : 12
        },
         {
            "nombre_ataque_magico" : "Canto mortal",
            "potencia" : 15
        }
    ]
}

monstruo = {
    "nombre"    :   "Eltermo",
    "hp"        : 30,
    "ataque"    : 70
}


def combate(datos_protagonista, datos_mosntruo):
    #opnstruo ataca primero
    datos_protagonista["hp"] = datos_protagonista["hp"]  - datos_mosntruo["ataque"]

    print(f"La vida del heroe luego del ataque es: { datos_protagonista["hp"]  }")
    
    #Que ataque eñl protagonista
    datos_mosntruo["hp"] = datos_mosntruo["hp"] - datos_protagonista["ataque"]
    print(f"La vida del montruo luego del ataque es: { datos_mosntruo["hp"]  }")

    if datos_mosntruo["hp"] <= 0:
        return "WIN"
    elif datos_protagonista["hp"] <= 0:
        return "LOSE"



while protagonista["hp"] > 0 and monstruo["hp"] > 0:
    resultado_combate = combate(protagonista, monstruo)
    if resultado_combate == "WIN":
        print("Ganaste")
    elif resultado_combate == "LOSE":
        print("Perdiste")
    else:
        print("*************Fin Turno, COMBATE SIGUE***************")
