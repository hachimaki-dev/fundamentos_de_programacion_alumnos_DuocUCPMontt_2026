def fighterShowcase(fighter):
    print("El nombre de el peleador es:")
    print(init_fighter_name(fighter))
    print("|----------------------------|")
    print("Su hp es de:")
    print (init_hp_bar(fighter))
    print("|----------------------------|")
    print("Y sus ataques son:")
    print(init_attack_moves(fighter))
    print("|----------------------------|")

def init_fighter_name(fighter):
    return fighter["name"]

def init_hp_bar(fighter):
    return fighter["hp"] * "|"

def init_attack_moves(fighter):
    return fighter["attacks"]


def fight(data_copper, data_thief):
    print(f"El policía se llama {data_copper["name"]}")
    print(f"El ladrón se llama {data_thief["name"]}")
cop = {
    "id" : "P-01",
    "name" : "Matias Moena",
    "hp" : 100,
    "attacks" : [
        {"attack_name" : "Pistola" , "attack_damage" : 50},
        {"attack_name" : "Lumazo" , "attack_damage" : 15}
    ]
}
human = {
    "id" : "H-01",
    "name" : "Micaela Torres",
    "hp" : 150,
    "attacks" : [
        {"attack_name" : "Pistola Eléctrica", "attack damage" : 50},
        {"attack_name" : "Posionous Cookie", "attack damage" : 40}
    ]   
}
thief = {
    "id" : "T-01",
    "name" : "Amaro López",
    "hp" : 70,
    "attacks" : [
        {"attack_name" : "Doble Navaja", "attack_damage" : 80},
        {"attack_name" : "Fists", "attack_damage" : 100}
    ]
}
fighterShowcase(cop)

fighterShowcase(human)

fighterShowcase(thief)
#fight(cop, thief)