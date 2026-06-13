protagonista = {
    'nombre':'Hernan Manoquemada',
    'Hp':100,
    'ataque':6,
    'magia':100,
    'ataques magicos':[
        {
        'ataque magico':'Bola de fuego',
        'daño':10
        },
        {
        'ataque magico':'Lluvia mágica',
        'daño':12
        },
        {
        'ataque magico':'Canto mortal',
        'daño':15
        }
    ]
}

monstruo = {
    'nombre':'Eltermo',
    'Hp':30,
    'ataque':7
}

def combate(datos_protagonista, datos_monstruo):
    #Monstruo ataca primero
    datos_protagonista['Hp'] = datos_protagonista['Hp'] - datos_monstruo['ataque']
    print(f"La vida del protagonista luego del ataque es {datos_protagonista['Hp']}")

    #Que ataque el protagonista
    datos_monstruo['Hp'] = datos_monstruo['Hp'] - datos_protagonista['ataque']
    print(f"La vida del monstruo luego del ataque es {datos_monstruo['Hp']}")

    if datos_monstruo['Hp'] <= 0:
        return "WIN :D"
    elif datos_protagonista['Hp'] <= 0:
        return "LOSE D:"


while protagonista['Hp'] > 0 and monstruo['Hp'] > 0:
    resultado_combate = combate(protagonista, monstruo)
    if resultado_combate == "WIN :D":
        print(resultado_combate)
    elif resultado_combate == "LOSE D:":
        print(resultado_combate)
    else:
        print("************* SIGUE EL COMBATE *************")