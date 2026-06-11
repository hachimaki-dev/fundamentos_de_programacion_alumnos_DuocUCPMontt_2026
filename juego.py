# WIP

import random

orpheus = {
    "ID": "P001",
    "Name": "Orpheus",
    "Level": 10,
    "HP": 100,
    "Agility": 20,
    "Skills": [
        {"SkillName": "Bash", "SkillType": "Phys", "SkillDamage": 25},
        {"SkillName": "Agi", "SkillType": "Fire", "SkillDamage": 30},
        {"SkillName": "Dia", "SkillType": "Heal", "SkillDamage": 30}
    ],
    "Weakness": "Ice"
}

izanagi = {
    "ID": "P002",
    "Name": "Izanagi",
    "Level": 12,
    "HP": 120,
    "Agility": 23,
    "Skills": [
        {"SkillName": "Slash", "SkillType": "Phys", "SkillDamage": 25},
        {"SkillName": "Zio", "SkillType": "Elec", "SkillDamage": 30}
    ],
    "Weakness": "Fire"
}
def battle_init(player_data, enemy_data):
    player_name = player_data["Name"]
    player_hp = player_data["HP"]
    enemy_name = enemy_data["Name"]
    enemy_hp = enemy_data["HP"]
    return player_name, player_hp, enemy_name, enemy_hp

def battle_status(player_name, enemy_name, player_current_hp, enemy_current_hp):
    print(f"{player_name} - HP: {player_current_hp} /// {enemy_name} - HP: {enemy_current_hp}\n")

def battle_choice_player(player_data):
    while True:
        print("HABILIDADES:")
        for i in range(len(player_data["Skills"])):
            print(f'{i + 1}. {player_data["Skills"][i]["SkillName"]}')
        try:
            player_choice = int(input("\nIngresa una habilidad: "))
            if (player_choice - 1) in range(len(player_data["Skills"])):
                break
            else:
                print("¡Ingresa un número válido!\n")
        except ValueError:
            print("¡Ingresa un número válido!\n")
    return player_choice - 1

def battle_choice_enemy(enemy_data):
    enemy_choice = random.randrange(len(enemy_data["Skills"]))
    return enemy_choice

def battle_loop (player_data, enemy_data):
    while True:
        player_name, player_hp, enemy_name, enemy_hp = battle_init(player_data, enemy_data)
        battle_status(player_name, enemy_name, player_hp, enemy_hp)
        if player_data["Agility"] > enemy_data["Agility"]:
            print(battle_choice_player(player_data))
            print(battle_choice_enemy(enemy_data))
        else:
            print(battle_choice_enemy(enemy_data))
            print(battle_choice_player(player_data))
        break
    
battle_loop(orpheus, izanagi)