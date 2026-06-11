def init_hp_bar(fighter):
    return fighter['hp'] * '/'

def init_id_fighter(fighter):
    return figther['id']

def init_fighter_name(fighter):
    return fighter['name']

def init_attacks_names(fighter):
    attack1_name = fighter['attacks'][0]['attack_name']
    attack2_name = fighter['attacks'][1]['attack_name']
    return attack1_name, attack2_name

def init_attacks_damage(fighter):
    attack1_damage = fighter['attacks'][0]['attack_damage']
    attack2_damage = fighter['attacks'][0]['attack_damage']
    return attack1_damage, attack2_damage

# Hagamos pelear al policia con el ladron
def fight(data_copper, data_thief):
    print(f"El policia se llama {data_copper['name']}")
    print(f"El ladron se llama {data_thief['name']}")


copper = {
    'id': 'P-01',
    'name': 'Matias Moena',
    'hp': 100,
    'attacks': [
        {'attack_name': 'Pistola', 'attack_damage': 90},
        {'attack_name': 'Lumazo', 'attack_damage': 15}
    ]
}

human = {
    'id': 'H-01',
    'name': 'Micaela Torres',
    'hp': 150,
    'attacks': [
        {'attack_name': 'Pistola Electrica', 'attack_damage': 50},
        {'attack_name': 'Galletita Venenosa', 'attack_damage': 40}
    ]
}

thief = {
    'id': 'T-01',
    'name': 'Amaro Lopez',
    'hp': 70,
    'attacks': [
        {'attack_name': 'Doble Navaja', 'attack_damage': 80},
        {'attack_name': 'Fist Punchi', 'attack_damage': 100}
    ]
}

