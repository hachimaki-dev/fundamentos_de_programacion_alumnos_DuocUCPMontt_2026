protagonista = {
    'Nombre' : 'Hernan manoquemada',
    'hp'     : 100,
    'ataque' : 6,
    'Magia'  : 100,
    'ataques_magicos' : [
        {
            'Nombre_ataque_magico' : 'bola de fuego', 'potencia' : 10
        },
        {
            'Nombre_ataque_magico' : 'Lluvia magica', 'potencia' : 12
        },
        {
            'Nombre_ataque_magico' : 'Canto mortal', 'potencia' : 15
        }
    ]
}
monstruo = {
    'Nombre' : 'Eltermo',
    'hp'     : 30,
    'ataque' : 7,
}
def combate(datos_protagonista, datos_monstruo):
    datos_protagonista["hp"] = datos_protagonista['hp'] - datos_monstruo['ataque']
    print(f"La vida del protagonista luego del ataque es: {datos_protagonista['hp']}")

    datos_monstruo['hp'] = datos_monstruo['hp'] - datos_protagonista['ataque']
    print(f"La vida del monstruo luego del ataque es: {datos_monstruo['hp']}")

    if datos_monstruo['hp'] <= 0 :
        return "Win"
    elif datos_protagonista['hp'] <= 0 :
        return "Lose"
    


while protagonista['hp']> 0 and monstruo['hp']> 0:
    resultado_combate = combate(protagonista, monstruo)
    if resultado_combate == "Win":
        print("ganaste")
    elif resultado_combate == "Lose":
        print("Perdiste")
    else:
        print("*************Fin de Turno, Combate sigue************")