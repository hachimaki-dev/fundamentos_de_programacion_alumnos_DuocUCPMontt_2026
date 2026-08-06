#17. Sistema de Combate RPG Crea atacar(atacante, defensor) recibiendo diccionarios de Stats. 
# Debe calcular evasión con random, reducir la vida del defensor mitigada por su armadura, 
# y retornar una tupla (nueva_vida, log_combate).
import random

luan = {
    "vida":100,
    "ataque":50,
    "armadura":20,
    "evasion":random.randint(1,10)
}
ordep = {
    "vida":100,
    "ataque":60,
    "armadura":30,
    "evasion":random.randint(1,10)
}
def atacar(atacante, defensor):
    for valor_atacante in atacante.values():
        for valor_defensor in defensor.values():
            valor_defensor[3] - valor_atacante[1]
            resto_de_ataque = valor_defensor[3] - valor_atacante[1]
            valor_defensor[0] - resto_de_ataque
    return defensor


pelea = atacar(luan,ordep)