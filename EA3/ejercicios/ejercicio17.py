#Crea atacar(atacante, defensor) recibiendo diccionarios de Stats. Debe calcular evasión con random, reducir la vida del defensor mitigada por su armadura, y retornar una tupla (nueva_vida, log_combate).
import random
def atacar(atacante, defensor):
    probabilidad_de_evasion = random.randint(0,100)
    if (defensor['evasion']) >= probabilidad_de_evasion:
        return (defensor['hp'],(f"{defensor['nombre']} ha evadido el ataque de {atacante['nombre']}"))
    else:
        ataque = (atacante['ataque'] - defensor['armadura'])
        if ataque < 1:
            ataque = 1
        defensor['hp'] -= ataque
        return (defensor['hp'],(f"{defensor['nombre']} ha sufrido {ataque} de daño por el ataque de {atacante['nombre']}"))
    
    
    
    


hero =  {
    'nombre' : 'Hero',
    'hp' : 100,
    'armadura' : 10,
    'ataque' : 16,
    'evasion' : 15
}

slime = {
    'nombre' : 'Slime',
    'hp' : 30,
    'armadura' : 6,
    'ataque' : 10,
    'evasion' : 5
}


nuevavida, log_combate = atacar(hero, slime)

print (log_combate)
print (nuevavida)