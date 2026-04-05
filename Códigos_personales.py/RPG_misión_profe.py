vida_jefe = 1000
ataque_espada = 200
ataque_mágico_fuego = 500
ataque_lluvia_helada = 0
desenvaine_solar = 400
elección = 0
numeros = 0
int(numeros in ['1', '2', '3', '4'])
print("En las heladas llanuras de los confines del reino...")
print("Un caballero descansa en una cueva entre tempanos de hielo. De pronto aparece UN YETI enojado. El caballero se pone a la defensiva y se prepara para atacar")

while vida_jefe >= 0:
    print(f"El jefe posee actualmente: {vida_jefe}")
    elección = int(input("""¿QUE ATAQUE DEBERÍA USAR EL CABALLERO?
                      (1) Desenvaine solar
                      (2) Ataque de fuego
                      (3) Corte rápido
                      (5) Lluvia helada"""))
    print(f"{vida_jefe}")
    
    if elección == 1:
        print("El caballero usa desenvaine solar y el jefe pierde 400 pts de vida")
        vida_jefe = vida_jefe - 400
    if elección == 2:
        print("El caballero usa ráfaga de fuego y el jefe pierde 400 pts de vida")
        vida_jefe = vida_jefe - 500
    if elección == 3:
        print("El caballero usa corte rápido y el jefe pierde 400 pts de vida")
        vida_jefe = vida_jefe - 200
    if elección == 4:
        print("El caballero usa lluvia helada, el jefe no sufre ningún daño ")
        vida_jefe = vida_jefe 
    else :
        print("")
   
    
    if vida_jefe == 0:
        print("HAS DERROTADO AL JEFE")
    else:
        print("")

print("El caballero derrota a la bestia y descansa de su travesía")
    
