def init_hp_bar(fighter):
    return fighter ["hp"] * "*"

def init_atacks(atacks):
    return atacks ["atacks"]

def init_fighters():
    return 

copper = {
    "id" : "P-01",
    "name" : "Matias Moena",
    "hp" : 100,
    "atacks" : [
        {"atack_name" : "Pistola" , "atack_damage" : 90},
        {"atack_name" : "Lumazo" , "atack_damage" : 15}
    ]
}

citizen = {
    "id" : "H-01",
    "name" : "Micaela Torres",
    "hp" : 150,
    "atacks" : [
        {"atack_name" : "Taser" , "atack_damage" : 50},
        {"atack_name" : "Poison Cookies" , "atack_damage" : 40}
    ]
}

thief = {
    "id" : "T-01",
    "name" : "Benjamin Miranda",
    "hp" : 100,
    "atacks" : [
        {"atack_name" : "Hacha" , "atack_damage" : 50},
        {"atack_name" : "Queque" , "atack_damage" : 30}
    ]
}

print(init_hp_bar())
init_atacks()
