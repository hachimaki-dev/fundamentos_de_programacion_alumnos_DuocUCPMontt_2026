protagonista = {
    'nombre' : 'Hernan mano quemada',
    'hp'     : 100,
    'ataque' : 6,
    'magia'  : 100,
    'ataque_magicos'  : [
        {
            'nombre_ataque_magico' : 'bola de fuego',
            'potencia'  : 10
        }, 
        {
            'nombre_ataque_magico' : 'lluvia magica',
            'potencia'  : 12
        },
        {
            'nombre_ataque_magico' : 'corte mortal',
            'potencia'  : 15
        }
    ]

    
}

monstruo = {
    'nombre'  :  'Eltermo',
    'hp'      :  30, 
    'ataque'  :  7
}



def combate(datos_protagonista, datos_monstruo):

    datos_protagonista['hp'] = datos_protagonista['hp'] -datos_monstruo['ataque']
    print(f'La vida luego del ataque es: {datos_protagonista['hp']}')

    datos_monstruo['hp'] = datos_monstruo['hp'] - datos_protagonista['ataque']
    print(f'La vida del monstruo luego del ataque es: {datos_monstruo['hp']}')

    if datos_monstruo['hp'] <= 0:
        return 'WIN'
    elif datos_protagonista ['hp'] <= 0:
        return 'LOSE'  

while protagonista['hp'] > 0 and monstruo['hp'] > 0:
    resultado_combate = combate(protagonista, monstruo)
    if resultado_combate == 'WIN':
        print('Ganaste')
    elif resultado_combate == 'LOSE':
        print('Perdiste')    
    else:
        print('Fin del combate')    