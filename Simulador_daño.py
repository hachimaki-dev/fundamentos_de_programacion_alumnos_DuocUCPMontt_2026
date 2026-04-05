vida_jefe_final= 1000

while vida_jefe_final>0:
    daño_del_usuario= int(input("Ingrese el daño de su ataque: "))
    if daño_del_usuario< 0:
        print("El ataque fallo")
    elif daño_del_usuario>= 0:
        vida_jefe_final-= daño_del_usuario
        print(f"La vida del jefe final es {vida_jefe_final}")
print("¡Jefe derrotado!")