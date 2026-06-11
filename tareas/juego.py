
def name_life_fighter(data_cooper):
    return data_cooper["life"]
def name_life_human(data_human):
    return data_cooper["life"]

def fight()

cooper = {
    "name_police" : "Policia",
    "life" : 100,
    "attacks" : [
        {
            "attacks_name" : "Pistola" , "attack_damage" : 90,
            "attacks_name" : "Palo electrico" , "attack_damage" : 40
        }
    ]
}
human = {
    "id" : "t-01",
    "name" : "npc",
    "life" : 70,
    "attacks" : [
        {
            "attacks_name" : None , "attack_damage" : 0,
            "attacks_name" : None , "attack_damage" : 0 
        }
    ]

}

while True:
    print("Bienvenido al mundo de la pelea")
    print("1 . Ver la vida del policia")
    print("2 . Ver la vida del Npc")
    print("Luchar!!")
    opcion_menu = input("Ingrese una opcion!")
    if opcion_menu == "1" : 
        print(f"la vida del policia es : {name_life_fighter(cooper)}")
    elif opcion_menu == "2":
        print(f"la vida del npc es {name_life_human(human)}")
    elif opcion_menu == "3":
        for i in range(3):
            