vida_jefe = 1000

print("****¡COMIENZA LA BATALLA!****")

while  vida_jefe > 0 :
    print(f"\nVida actual del jefe: {vida_jefe}")
    
    ataque = int(input("ingrese el daño de su ataque: "))
    if ataque < 0:
        print("¡el ataque fallo!(no puedes hacer daño negativo")
    else:
        vida_jefe = vida_jefe - ataque
        print(f"¡le diste! hiciste {ataque} de daño")
        
        print("\n*********************")
        print("¡JEFE DERROTADO!")
        print("***********************")

#ayuda de ia
