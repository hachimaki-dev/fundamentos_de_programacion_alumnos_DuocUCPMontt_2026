
def init_hp_bar(figther):
    return figther["hp"] * "/"

def datos_personaje(datos):
    print("Los datos Del Personaje Son:\n")

def fight(data_copper, data_thief ):
    print(f"El policia se llama {data_copper["name"]}")
    print(f"El ladrón se llama {data_thief["name"]}")

copper = {
    "id" : "P-01",
    "name" : "Matias Moena",
    "hp"  : 100,
    "attacks" : [
    {"attack_name" : "Pistola", "attack_damage" : 90},
    {"attack_name" : "Lumazo", "attack_damage" : 15}
    ]
}

human = {
    "id" : "H-01",
    "name" : "Micaela Torres",
    "hp"  : 150,
    "attacks" : [
    {"attack_name" : "Pistola Electrica!", "attack_damage" : 50},
    {"attack_name" : "Poison coockie", "attack_damage" : 40}
    ]
}

thief = {
    "id" : "T-01",
    "name" : "Amaro Lopez",
    "hp"  : 70,
    "attacks" : [
    {"attack_name" : "Doble Navaja", "attack_damage" : 80},
    {"attack_name" : "Fist Punchi!", "attack_damage" : 100}
    ]
}



print(init_hp_bar(human))

#Debajito de la barra de vida, colocar la info del jugaor., nombre, sus ataques y su correspondiente daño