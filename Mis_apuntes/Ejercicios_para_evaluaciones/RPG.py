#SIMULADOR DE DAÑO RPG

hp = 1000   #SE DA EL VALOR DE LA VIDA DEL JEFE
while hp > 0:
    dmg = int(input("Cuanto daño haras? "))
    if dmg < 0:
        print("Fallaste.")
    elif dmg > 0:
        hp = hp - dmg
        print(f"Al jefe le quedan {hp} puntos de vida restantes.")
print("Jefe derrotado")