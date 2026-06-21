import random
def atacar(atacante, defensor):
    suerte = random.randint(1, 100)
    if suerte <= defensor['evasion']:
        log_combate = "El defensor esquivo el ataque!!"
        return (defensor['vida'], log_combate)
    daño = atacante['ataque'] - defensor['armadura']
    if daño < 0:
        daño = 0
    nueva_vida = defensor['vida'] - daño
    if nueva_vida < 0:
        nueva_vida = 0
    log_combate = f"ataque exitoso, se inflingio {daño} de daño "
    return(nueva_vida, log_combate)
protagonista = {'vida'    : 120,
                'ataque'  : 30,
                'armadura': 10,
                'evasion' : 20}
mounstro = {    'vida'    : 90,
                'ataque'  : 25,
                'armadura': 5,
                'evasion' : 10}
nuevda_vida_enemigo, registro = atacar(atacante=protagonista, defensor=mounstro)
print(registro)
print(nuevda_vida_enemigo)