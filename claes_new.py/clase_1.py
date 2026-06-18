def init_name(nombre):
    return nombre["Name"]

def init_life(vida):
    return vida["Hp"] * "/"

def init_attack(ataque):
    return ataque["Attacks"]

#hagamos pelear el Policia contra el Ladron
def figth(data_copper, data_thief):
    print(f"El policia se llama{data_copper["name"]}")
    print(f"El Ladron se llama{data_thief["name"]}")

copper = {
    "ID" : "P-01",
    "Name" : "Benso Brandon",
    "Hp" : 100,
    "Attacks": [
        {"attack_name" : "Pistola", "attack_danage" : 90},
        {"attack_name" : "Lumazo", "attack_danage" : 15}
    ]
}

human = {
    "ID" : "H-01",
    "Name" : "Wilson Rubius",
    "Hp" : 150,
    "Attacks": [
        {"attack_name" : "Pistola Eletrica", "attack_danage" : 50},
        {"attack_name" : "Poison coockie", "attack_danage" : 40}
    ]
}

thief = {
    "ID" : "T-01",
    "Name" : "Gutierres Sanbernando",
    "Hp" : 70,
    "Attacks": [
        {"attack_name" : "Doble Navaja", "attack_danage" : 80},
        {"attack_name" : "Fist Punchil", "attack_danage" : 100}
    ]
}

print()
print(init_name(copper))
print()
print(init_life(copper))
print()
print(init_attack(copper))
print()

#figth(copper, thief)