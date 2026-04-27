



print(">>>>>> LA LEYENDA DE NUESTRO PRIMER HEROE<<<<<<")

print("PARTE 1 >>>> ENCONTRAMOS AL HEROE <<<<")




nombre_heroe = input("Hola, Cual es tu nombre candidato a heroe: ")
print(f"Hola {nombre_heroe}. Al fin  llega el dia en que te pudimos encontrar, justo a tiempo. vaya de verdad que te ves muy Debil,\n" \
     "Temeroso,un poco Vergonzoso para ser el Candidato a Heroe,pero bueno quizas aun no desarrollas todo tu potencial\n" \
     " continuemos... \n"\
     "Porque Tienes una gran mision y tu destino esta por Cambiar y  Brillar,es lo que siempre haz soñado con darle un giro emocionante a tu vida, \n" \
     "entonces solo me queda preguntarte.. ¿Quieres vovlerte mas fuerte, convertirte en el heroe que necesitamos y  derrotar al Rey Demonio ? ")



# estadisticas personajes

estadisticas_heroe = {"vida_heroe":100, "fuerza":10, "agilidad":20, "mana":5, "defensa": 50}

estadisticas_rey_demonio = {"vida_Rey_demonio":200, "fuerza":120, "agilidad":160, "mana":120, "defensa": 90}



print("PARTE 2>>>> BIENVENIDO A TU ENTRENAMIENTO <<<<")





estadisticas = input("¿quieres revisar tus estadisticas ? si/no: ").strip().lower() 
if estadisticas == "si":
    for clave, valor in estadisticas_heroe.items():
        print(f"{clave}:{valor}")
            

elif estadisticas ==  "no":
    print("en otra ocasion sera")
    exit()

            
else:
    print("valor ingresado, no valido")
    exit()
            
        

while True:

    entrenamiento = input("Ahora debes realizar el entrenamiento para ser un heroe... cuentame..¿que dicision vas a tomar?: si/no ").strip().lower() 
    if entrenamiento == "si":
        print("bienvenido, no sera facil, pero aumentaras tus estadisticas \npara poder ser una Heroe que se convierte en Leyenda....aun queda mucho camino!!")
        print("han pasado 2 años desde tu entrenamiento.....")
        estadisticas_heroe.update({"vida_heroe":150,"fuerza":100,"agilidad":120,"mana":90,"defensa":60})      

       
          

    elif entrenamiento == "no":
        print("valla no me esperaba esa respuesta dejaremos a la humanidad a merced del rey Demonio, cuidate muchacho y sobrevive")
        print("ESTE FUE EL FIN DE LA HUMANIDAD, YA NO EXISTE NADA")  
                    
                    
                
    else:
        print("valor ingresado, no valido")
            
    
    while True:       
        estadisticas = input("¿quieres revisar los Resultados de tu entrenamiento,¿quieres tus  nuevas estadisticas? si/no:  ").strip().lower()   
        if estadisticas == "si":
            print(estadisticas_heroe)
                
                    
        elif estadisticas == "no":
            print("en otra ocasion sera")
                        
                    
        else:
            print("valor no válido")
            continue

        



        print(")parte 3 >>>> las batalla comienza <<<<")
        print("llego el gran dia")
                    
        vida_heroe = 150
        vida_rey_demonio = 200

        ataques_heroe = [("1.blandir espada: 10"),("2.hechizo de fuego: 20"),("3.golpe de puño: 5")]
        defensa_heroe = [("1.defender: 30"), ("2.curacion: 15")]

        print(f"(tus ataques son {ataques_heroe}")



        while vida_heroe > 0 and vida_rey_demonio > 0:
       



            ataques_demonio = [("1.rayo oscuro: 20"),("2.hachazo: 25"),("3.espada oscura: 30"),("4.puño sombra: 25")]
            defensa_demonio =  [("1.defender:50"), ("2.curacion: 35")]

            
            atacar = int(input("es hora,elige tu ataque: ")) 
                            
            if atacar == 1:
                print(f"haz elegido blandir espada, le haz quitado 10 de vida, le queda un total de {vida_rey_demonio -10} vida\n el rey demonio ataca con hachazo,te quita 25 te queda {vida_heroe-25}vida")
                vida_rey_demonio -=  10
                vida_heroe -=  25
                print(f"vida heroe: {vida_heroe}")
                print(f"vida rey demonio: {vida_rey_demonio}")

            elif atacar == 2:
                print(f"haz elegido[2], le haz quitado 20 de vida, le queda un total de {vida_rey_demonio-20} vida\nel rey demonio te ataca con espada oscura te quita 30 de vida te queda un total de {vida_heroe-30} vida")
                vida_heroe -= 30
                vida_rey_demonio -= 20
                print(f"vida heroe: {vida_heroe}")
                print(f"vida rey demonio: {vida_rey_demonio}")

            elif atacar == 3:
                print(f"haz elegido golpe de puño le haz quitado 5 de vida, le queda un total de {vida_rey_demonio-5} vida\n el rey demonio te ataca con puño somnbra y te quita 25 de vida, te queda un total de{vida_heroe-25}vida")
                vida_rey_demonio -=  5
                vida_heroe -=  25
                print(f"vida heroe: {vida_heroe}")
                print(f"vida rey demonio: {vida_rey_demonio}")
                    
            else: 
                print("ataque no valido")
                continue


            print(f"vida heroe: {vida_heroe}")
            print(f"vida rey demonio: {vida_rey_demonio}")
                    

            if vida_heroe <= 20:
                print(f"te queda poca vida, estas a punto de morir, justo cuando estas a punto de ser aniquilado\nun destello aparece junto a ti es un item raro... valla es la espada celestial, la diosa te a bendecido, quieres ver usar este nuevo item ")
                                
                blandir_doble = input("quieres usar blandir doble: si/no: ").strip().lower()
                if blandir_doble == "si":
                    vida_rey_demonio =  0
                    print(f"te levantas debilmente decides tomar el item y usarlo tu vida tu status se reinicia miras fijamente al demonio\nte resplandece un aura brillante activas blandir doble ejecutas el ataque\ndas un golpe de 100 hits la vida del rey demonio cae rapidamente\n ha sido derrotado al fin\n quieres verificar si realmente esta muerto su vida llego a {vida_rey_demonio-vida_rey_demonio} vida")
                    if vida_rey_demonio <= 0:
                        print("haz derrotado al rey demonio, al fin la humanidad vvira la paz que tanto anhelaba")
                        continue
                else:
                    print("haz muerto, y no lograste tu objetivo")
                    break
                if vida_heroe<= 0:
                    print("haz sido derrotado y con ello el fin de este mundo")
                    

                
                print(f"felicidades lograste derrotar al rey demonio es una gran proeza junto con la bendicion de la espada celestial, sin dudad ahora te haz convertido en una leyenda {nombre_heroe}")
                exit()
                                    
                    
            
        