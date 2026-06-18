import random

# =====================
# PERSONAJES
# =====================

copper = {
    "ID": "P-01",
    "Name": "Benso Brandon",
    "Hp": 100,
    "Attacks": [
        {"attack_name": "Pistola", "attack_damage": 90},
        {"attack_name": "Lumazo", "attack_damage": 15}
    ]
}

human = {
    "ID": "H-01",
    "Name": "Wilson Rubius",
    "Hp": 150,
    "Attacks": [
        {"attack_name": "Pistola Eléctrica", "attack_damage": 50},
        {"attack_name": "Poison Cookie", "attack_damage": 40}
    ]
}

thief = {
    "ID": "T-01",
    "Name": "Gutierres Sanbernando",
    "Hp": 70,
    "Attacks": [
        {"attack_name": "Doble Navaja", "attack_damage": 80},
        {"attack_name": "Fist Punchil", "attack_damage": 100}
    ]
}

characters = [copper, human, thief]

# =====================
# BARRA DE VIDA
# =====================

def hp_bar(hp, max_hp):
    barras = int((hp / max_hp) * 20)
    return "🟩" * barras + "⬜" * (20 - barras)

# =====================
# SELECCIONAR PERSONAJE
# =====================

print("\n🎮 ===== ARENA DE COMBATE ===== 🎮\n")

for i, character in enumerate(characters):
    print(f"{i+1}. {character['Name']} ❤️ {character['Hp']} HP")

player_choice = int(input("\n👉 Elige tu personaje: ")) - 1

player = characters[player_choice]

print("\n🎯 Elige un oponente:\n")

opponents = []

for character in characters:
    if character != player:
        opponents.append(character)

for i, enemy in enumerate(opponents):
    print(f"{i+1}. {enemy['Name']}")

enemy_choice = int(input("\n⚔️ Contra quién lucharás: ")) - 1

enemy = opponents[enemy_choice]

# Copias para no modificar originales
player_hp = player["Hp"]
enemy_hp = enemy["Hp"]

player_max_hp = player_hp
enemy_max_hp = enemy_hp

# =====================
# COMBATE
# =====================

print("\n🔥 ¡COMIENZA LA BATALLA! 🔥\n")

while player_hp > 0 and enemy_hp > 0:

    print("=" * 50)
    print(f"🧑 {player['Name']}")
    print(f"❤️ {player_hp}/{player_max_hp}")
    print(hp_bar(player_hp, player_max_hp))

    print()

    print(f"👹 {enemy['Name']}")
    print(f"❤️ {enemy_hp}/{enemy_max_hp}")
    print(hp_bar(enemy_hp, enemy_max_hp))
    print("=" * 50)

    print("\n⚔️ ATAQUES DISPONIBLES:\n")

    for i, attack in enumerate(player["Attacks"]):
        print(
            f"{i+1}. {attack['attack_name']} "
            f"({attack['attack_damage']} daño)"
        )

    attack_choice = int(input("\n👉 Escoge un ataque: ")) - 1

    selected_attack = player["Attacks"][attack_choice]

    damage = selected_attack["attack_damage"]

    enemy_hp -= damage

    print(
        f"\n💥 {player['Name']} usa "
        f"{selected_attack['attack_name']}"
    )
    print(f"🔥 Hace {damage} de daño")

    if enemy_hp <= 0:
        enemy_hp = 0
        print(f"\n🏆 ¡{player['Name']} ha ganado!")
        break

    # Turno enemigo
    enemy_attack = random.choice(enemy["Attacks"])

    damage = enemy_attack["attack_damage"]

    player_hp -= damage

    print(
        f"\n👹 {enemy['Name']} usa "
        f"{enemy_attack['attack_name']}"
    )
    print(f"💥 Hace {damage} de daño")

    if player_hp <= 0:
        player_hp = 0
        print(f"\n☠️ ¡{enemy['Name']} ha ganado!")
        break

    input("\n⏭️ Presiona ENTER para continuar...")