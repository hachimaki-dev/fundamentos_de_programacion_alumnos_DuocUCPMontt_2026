#Variables
Combate = True
Error= "Opcion Invalida"
Fase1=False
Fase2=False
Fase3=False
Pokemon1 = "Heatmor"
Pokemon2 = "Cryonogal"
Pokemon3 = "Granbull"
PokemonRival1 = "Spiritomb" #Hada x2 otros neutro
PokemonRival2 = "Lucario" #Fuego x2 Hada x0.5 Hielo x0.5
PokemonRival3 = "Garchomp" #hielo x4 Hada x2 fuego x0.25
VidaPokemon1 = 20
VidaPokemon2 = 20
VidaPokemon3 = 20
VidaPokemonRival1 = 20
VidaPokemonRival2 = 20
VidaPokemonRival3 = 20

Combate = True
while Combate == True:
    if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
            break
    print ("""                                   ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
LA CAMPEONA CYNTHIA TE DESAFIA A UN COMBATE""")

# Spirtomb
    Fase1 = True
    print("Cynthia envia a Spiritomb")
    while Fase1 == True:
        Opcion = 0
        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
            Combate = False
            break
        else:
            Opcion =int(input("""Seleccione uno de los siguientes pokemon:
                            1) Heatmor
                            2) Cryogonal
                            3) Granbull
                            """))
        #OPCION HEATMOR (NO EFECTIVO)    
        while Opcion == 1:
                if VidaPokemon1 <= 0:
                     print (Error)
                     break
                else:
                    print (f"{Pokemon1} tiene {VidaPokemon1} puntos de vida \n {PokemonRival1} tiene {VidaPokemonRival1} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon1}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon1} atacó a {PokemonRival1}")
                        VidaPokemonRival1 = VidaPokemonRival1-5
                        print(f"Ataque neutral")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break
                        
                                    
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    if VidaPokemonRival1>0:
                        print(f"{PokemonRival1} ataco a {Pokemon1}")
                        VidaPokemon1 = VidaPokemon1-5
                        print(f"Ataque neutral")
                    if VidaPokemon1 <= 0 or VidaPokemonRival1 <= 0:
                        if VidaPokemon1 <= 0:
                            print(f"{Pokemon1} se ha debilitado")
                    
                        if VidaPokemonRival1 <= 0:
                            Fase1= False
                            Fase2= True
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False
                         
                        break
                    
                
        #OPCION CRYOGONAL (NO EFECTIVO)    
        while Opcion == 2:
                if VidaPokemon2 <= 0:
                     print (Error)
                     break
                else:     
                    print (f"{Pokemon2} tiene {VidaPokemon2} puntos de vida \n {PokemonRival1} tiene {VidaPokemonRival1} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon2}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon2} atacó a {PokemonRival1}")
                        VidaPokemonRival1 = VidaPokemonRival1-5
                        print(f"Ataque neutral")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    if VidaPokemonRival1>0:
                        print(f"{PokemonRival1} ataco a {Pokemon2}")
                        VidaPokemon2 = VidaPokemon2-5
                        print(f"Ataque neutral")     
                    if VidaPokemon2 <= 0 or VidaPokemonRival1 <= 0:
                        if VidaPokemon2 <= 0:
                            print(f"{Pokemon2} se ha debilitado")
                    
                        if VidaPokemonRival1 <= 0:
                            Fase1= False
                            Fase2= True 
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False    
                        break  
        #OPCION GRANBULL (EFECTIVO)
        while Opcion == 3:
                if VidaPokemon3 <= 0:
                    print(Error)
                    break
                else:
                    print (f"{Pokemon3} tiene {VidaPokemon3} puntos de vida \n {PokemonRival1} tiene {VidaPokemonRival1} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon3}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon3} atacó a {PokemonRival1}")
                        VidaPokemonRival1 = VidaPokemonRival1-10
                        print(f"Ataque Eficaz")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    if VidaPokemonRival1>0:
                        print(f"{PokemonRival1} ataco a {Pokemon3}")
                        VidaPokemon3 = VidaPokemon3-2
                        print(f"Ataque poco eficaz")
                    if VidaPokemon3 <= 0 or VidaPokemonRival1 <= 0:
                        if VidaPokemon3 <= 0:
                            print(f"{Pokemon3} se ha debilitado")
                    
                        if VidaPokemonRival1 <= 0:
                            Fase1= False
                            Fase2= True 
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False 
                                 
                        break
                    
                 
        
        
          
#Lucario
    while Fase2 == True:
        print("Spiritomb se ha debilitado")
        ##print(f"DEBUG{VidaPokemon1+VidaPokemon2+VidaPokemon3}")
        print("Cynthia envia a Lucario")
        Opcion = 0
        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
            Combate = False
            break
        else:
            Opcion = int(input("""Seleccione uno de los siguientes pokemon:
                            1) Heatmor
                            2) Cryogonal
                            3) Granbull
                            """))
        #OPCION HEATMOR (EFECTIVO)    
        while Opcion == 1:
                if VidaPokemon1 <= 0:
                     print (Error)
                     break
                else:
                    print (f"{Pokemon1} tiene {VidaPokemon1} puntos de vida \n {PokemonRival2} tiene {VidaPokemonRival2} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon1}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon1} atacó a {PokemonRival2}")
                        VidaPokemonRival2 = VidaPokemonRival2-10
                        print(f"Tu ha ataque ha sido eficaz")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break
                        
                                    
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    if VidaPokemonRival2>0:
                        print(f"{PokemonRival2} ataco a {Pokemon1}")
                        VidaPokemon1 = VidaPokemon1-5
                        print(f"Ataque neutral")
                if VidaPokemonRival2 <= 0 or VidaPokemon1 <=0:
                    if VidaPokemon1 <= 0:
                            print(f"{Pokemon1} se ha debilitado")
                            
                    
                    if VidaPokemonRival2 <= 0: 
                        Fase2= False
                        Fase3= True
                    if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False      
                    break
        #OPCION CRYOGONAL (DEBIL)
        while Opcion == 2:
                if VidaPokemon2 <= 0:
                     print(Error)
                     break
                else:
                    print (f"{Pokemon2} tiene {VidaPokemon2} puntos de vida \n {PokemonRival2} tiene {VidaPokemonRival2} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon2}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon2} atacó a {PokemonRival2}")
                        VidaPokemonRival2 = VidaPokemonRival2-2
                        print(f"Ataque Poco Eficaz")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    print(f"{PokemonRival2} ataco a {Pokemon2}")
                    
                    VidaPokemon2 = VidaPokemon2-10
                    print(f"Ataque Eficaz")
                    if VidaPokemon2 <= 0 or VidaPokemonRival2 <= 0:
                        if VidaPokemon2 <= 0:
                            print(f"{Pokemon2} se ha debilitado")
                    
                        if VidaPokemonRival2 <= 0: 
                            Fase2= False
                            Fase3= True
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False      
                        break
        #OPCION GRANBULL (MUY POCO EFICAZ)
        while Opcion == 3:
                if VidaPokemon3 <= 0:
                     print(Error)
                     break
                else:
                    print (f"{Pokemon3} tiene {VidaPokemon3} puntos de vida \n {PokemonRival2} tiene {VidaPokemonRival2} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon3}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon3} atacó a {PokemonRival2}")
                        VidaPokemonRival2 = VidaPokemonRival2-2
                        print(f"Ataque poco eficaz")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    if VidaPokemonRival2>0:
                        print(f"{PokemonRival2} ataco a {Pokemon3}")
                        VidaPokemon3 = VidaPokemon3-10
                        print(f"Ataque eficaz")
                
                    if VidaPokemon3 <= 0 or VidaPokemonRival2 <= 0:
                        if VidaPokemon3 <= 0:
                            print(f"{Pokemon3} se ha debilitado")
                    
                        if VidaPokemonRival2 <= 0:
                            Fase1= False
                            Fase2= True 
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False      
                        break               
             
             
#garchomp
    while Fase3 == True:
        print ("Lucario enemigo se ha debilitado ")
        print("Cynthia envia a Garchomp")
        Opcion = 0
        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
            Combate = False
            break
        else:
            Opcion = int(input("""Seleccione uno de los siguientes pokemon:
                            1) Heatmor
                            2) Cryogonal
                            3) Granbull
                            """))
    #OPCION HEATMOR (MUY POCO EFICAZ MUERES)    
        while Opcion == 1:
                if VidaPokemon1 <= 0:
                     print (Error)
                     break
                else:
                    print (f"{Pokemon1} tiene {VidaPokemon1} puntos de vida \n {PokemonRival3} tiene {VidaPokemonRival3} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon1}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon1} atacó a {PokemonRival3}")
                        VidaPokemonRival3 = VidaPokemonRival3-1
                        print(f"Ataque poco eficaz")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break
                        
                                    
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    
                    
                    if VidaPokemonRival3 > 0:
                        print(f"{PokemonRival3} ataco a {Pokemon1}")
                        print("ES SUPER EFICAZ")
                        VidaPokemon1 = VidaPokemon1-20
                    if VidaPokemonRival3 <= 0 or VidaPokemon1 <=0:
                        if VidaPokemon1 <= 0:
                            print(f"{Pokemon1} se ha debilitado")
                    
                        if VidaPokemonRival3 <= 0:
                    
                            Fase3= False
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False      
                        break
        #OPCION CRYOGONAL (SUPER EFICAZ)
        while Opcion == 2:
                if VidaPokemon2 <= 0:
                     print(Error)
                     break
                else:
                    print (f"{Pokemon2} tiene {VidaPokemon2} puntos de vida \n {PokemonRival3} tiene {VidaPokemonRival3} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon2}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon2} atacó a {PokemonRival3}")
                        VidaPokemonRival3 = VidaPokemonRival3-20
                        print("Ataque Super eficaz")                    
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    
                    
                    if VidaPokemonRival3 > 0:
                        print(f"{PokemonRival3} ataco a {Pokemon2}")
                    
                        VidaPokemon2 = VidaPokemon2-10
                        print(f"Ataque eficaz")
                    if VidaPokemonRival3 <= 0 or VidaPokemon2 <=0:
                        if VidaPokemon2 <= 0:
                            print(f"{Pokemon2} se ha debilitado")
                    
                        if VidaPokemonRival3 <= 0:
                    
                            Fase3= False
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False      
                        break
        #OPCION GRANBULL ( EFICAZ)
        while Opcion == 3:
                if VidaPokemon3 <= 0:
                     print(Error)
                     break
                else:
                    print (f"{Pokemon3} tiene {VidaPokemon3} puntos de vida \n {PokemonRival3} tiene {VidaPokemonRival3} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon3}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon3} atacó a {PokemonRival3}")
                        VidaPokemonRival3 = VidaPokemonRival3-10
                        print(f"Ataque eficaz")
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        break                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    if VidaPokemonRival3 > 0:
                        print(f"{PokemonRival3} ataco a {Pokemon3}")
                        VidaPokemon3 = VidaPokemon3-10
                        print(f"Ataque eficaz")
                    if VidaPokemonRival3 <= 0 or VidaPokemon3 <=0:
                        if VidaPokemon3 <= 0:
                            print(f"{Pokemon3} se ha debilitado")
                    
                        if VidaPokemonRival3 <= 0:
                    
                            Fase3= False
                        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
                            Combate = False      
                        break
    if (VidaPokemonRival3)< 0:
        print("Garchomp se ha debilidaado")
    
    if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0 or (VidaPokemonRival1+VidaPokemonRival2+VidaPokemonRival3) <= 0:
        Combate = False

print(f"\nCombate terminado")
if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
    print("Has perdido")
else:
    print("Has ganado")       


 





