"""
def saludar (nombre): #Parametro son opcionales
    print(f"Hola {nombre} ¿como estas?")
    return "1000 de aura" #Return igual es opcional

#saludar("Nami") #Argumento le puedes pasar cualquier tipo de dato para llamar al argumento

respuesta = saludar ("Nami")
print(f"La respuesta es {respuesta}")
"""

protagonista = {
    "Nombre": "Hernan Manoquemada",
    "hp": 100,
    "Ataque": 6,
    "Magia": 100,
    "Ataques_magicos": [
        {
            "Nombre_ataque_magico": "Bola de fuego",
            "Potencia" : 10
        },
        {
            "Nombre_ataque_magico": "Lluvia Magica",
            "Potencia" : 12
        },
        {
            "Nombre_ataque_magico": "Canto mortal",
            "Potencia" : 15
        }
    ]

}

monstruo = {
    "Nombre": "Elterno",
    "Hp": 30,
    "Ataque": 7
}

def combate(datos_protagonista, datos_monstruo):
    datos_protagonista["hp"] = datos_protagonista["hp"] - datos_monstruo["Ataque"]
    print(f"La vida despues del ataque del protagonista es: {datos_protagonista["hp"]}")
    datos_monstruo["Hp"] = datos_monstruo["Hp"] - datos_protagonista["Ataque"]
    print(f"La vida del Jefe despues del ataque es: {datos_monstruo["Hp"]}")

    if datos_monstruo["Hp"] == 0:
        return "WIN"
    elif datos_protagonista["hp"] == 0:
        return "LOSE"

while protagonista["hp"] > 0 and monstruo["Hp"] > 0:
    resulta_combate = combate(protagonista,monstruo)
    if resulta_combate == "WIN":
        print("Ganaste")
    elif resulta_combate == "LOSE":
        print("Perdiste")
    else:
        print("-----------Fin turno, COMBATE SIGUE----------")

                              

