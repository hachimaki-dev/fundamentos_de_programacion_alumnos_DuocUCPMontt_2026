rasen_shuriken = 200
chidogan = 300
super_genkidama = 400
vida_jugador = 2000
vida_jefe2 = 2000
nombre_jugador = "matias"

print(" la vida del jefe es de 2000")
print(f" 1.rasen_shuriken {rasen_shuriken} de daño")
print(f"2.chidogan {chidogan} de daño")
print(f"3.super genkidama {super_genkidama} de daño")

while vida_jefe2 > 0:
    ataque = input("Escoge una habilidad")
    print("")
    if ataque == "1":
        vida_jefe2 = vida_jefe2 - rasen_shuriken
        print(f"Has infligido {rasen_shuriken} Ptos de daño.")
        print("")
       
        print(f"---Darkorus---HP:{vida_jefe2}---")
        print("")
        

    elif ataque == "2":
        vida_jefe2 = vida_jefe2 - chidogan
        print(f"Has infligido {chidogan} Ptos de daño.")
        print("")
        
        print(f"---Darkorus---HP:{vida_jefe2}---")
        print("")
       

    
    elif ataque == "3":
        vida_jefe2 = vida_jefe2 - chidogan
        print(f"Has infligido {super_genkidama} Ptos de daño.")
        print("")
        
        print(f"---Darkorus---HP:{vida_jefe2}---")
        print("")
        
    
    
    
    else:
        print("Ataque nulo. Pierdes un turno")
        print("")
        
        print(f"HP:{vida_jefe2}")
        print("")
        
    

    if vida_jefe2 > 0:
        
         vida_jugador = vida_jugador - 200
         print("")
         
         print(f"Te han inflingido 100 Ptos de daño.")
         print("")
         
         print(f"---{nombre_jugador}---HP:{vida_jugador}")
         print("")
         

