boss_hp = 1000

while boss_hp > 0:
    dano_user = int(input("Ingresa el daño que quieres hacer: "))
    if dano_user <= 0:
        print("¡El ataque falló!")
    else:
        boss_hp -= dano_user
        print(f"Vida restante del jefe: {boss_hp}")

print("¡Jefe derrotado!, Ganaste")