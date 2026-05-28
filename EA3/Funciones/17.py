import random

def attack(attacker: dict[str, int], defender: dict[str, int]) -> tuple[int, str]:
    evasion = random.randint(1,100) <= 5

    if evasion:
        return (defender["hp"], "El defensor evadió el ataque")
    
    damage_dealed = attacker["damage"] - defender["armor"]
    new_defender_hp = defender["hp"] - damage_dealed

    log_report = f"El defensor recibió {damage_dealed} de daño, vida restante: {new_defender_hp}"
    return (new_defender_hp, log_report)

atacante = {
    "hp": 100,
    "damage": 25,
    "armor": 10
}

defensor = {
    "hp": 100,
    "damage": 10,
    "armor": 5
}

print(attack(atacante, defensor))