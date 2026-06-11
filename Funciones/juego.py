def init_hp_bar(fighter):
    return fighter["hp"] * "|" 

def init_name(fighter):
    return fighter["name"]

def init_id(fighter):
    return fighter["id"]

def init_attacks(fighter):
    return fighter["attacks"]


#Hagamos pelear al policia con el ladrón
def fight(data_copper, data_thief):
    print(f"El policia se llama {data_copper["name"]}")
    print(f"El policia se llama {data_thief["name"]}")
copper = {
    "id" : "P-01",
    "name" : "Matias Moena",
    "hp" : 100,
    "attacks" : [
        {"attack_name" : "Pistola", "attack_damage" : 90},
        {"attack_name" : "Lumazo", "attack_damage" : 15}
    ]
}

human = {
    "id" : "H-01",
    "name" : "Micaela Torres",
    "hp" : 150,
    "attacks" : [
        {"attack_name" : "Pistola Electrica", "attack_damage" : 50},
        {"attack_name" : "Poison cookie", "attack_damage" : 40}
    ]
}

thief = {
    "id" : "T-01",
    "name" : "Amaro Lopez",
    "hp" : 70,
    "attacks" : [
        {"attack_name" : "Doble Navaja", "attack_damage" : 80},
        {"attack_name" : "Fist punchi!", "attack_damage" : 100}
    ]
}

name = init_name(copper)
attacks = init_attacks(copper)
id = init_id(copper)
hp = init_hp_bar(copper)




print(name)
print(id)
print(attacks)
print(hp)