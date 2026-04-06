# TERMINADO

vida_jefe_final = 1000

print("================================")
print("===== ¡MATA AL JEFE FINAL! ===== ")
print("================================")

while vida_jefe_final > 0:
    print(f"\nVida del jefe: {vida_jefe_final} HP")
    
    cantidad_daño = int(input("¿Cuánto daño tiene tu ataque?: "))
    atacar = input("¿Disparar? (si/no): ")

    if atacar == "si":
        vida_jefe_final -= cantidad_daño
        print(f" ¡Impacto! Le quitaste {cantidad_daño} de vida.")

        if vida_jefe_final <= 0:
            break

        print("¡SIGUE ASÍ!")
        
        seguir_atacando = input("¿Lanzar combo extra de 100? (si/no): ")
        
        if seguir_atacando == "si":
            vida_jefe_final -= 100
            print(" ¡BOOM!")
            
            if vida_jefe_final <= 0:
                break
            
            print(f"Vida restante: {vida_jefe_final}")
            print("¡ATACAAAAAAAA!")
    else:
        print(" No atacaste :o")

print("================================")
print("¡EL JEFE HA SIDO DERROTADO! ")
print("===== ¡GANASTE EL JUEGO! >:3 =====")
print("================================")