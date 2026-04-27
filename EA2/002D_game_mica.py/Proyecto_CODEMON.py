print(r"""
   ██████╗  ██████╗ ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
  ██╔════╝ ██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
  ██║      ██║   ██║██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
  ██║      ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
  ╚██████╗ ╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
   ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 
                 ╔══════════════════════════════╗
                 ║ HISTORIA • COMBATE • AVENTURA║
                 ╚══════════════════════════════╝

           ▸ ESCRIBE TU LEYENDA. UNA LÍNEA A LA VEZ ◂

""")

print("( Cuando termine de leer cada linea de texto vaya Presionando Enter )")
input("Presione Enter para Continuar. . .")
print("♪quiero programar sin parar♪")
print("♪ser el mejor en compilar♪")
print("♪codemon es mi misión♪")
print("♪arreglar errores es la evolución♪")
input("Presiona ENTER para continuar...")
print()
print("Bienvenido a codemon")
input()
print("aquí los programadores capturan criaturas llamadas codemon")
input()
print("cada codemon tiene habilidades únicas ")
input()
print("tu misión es convertirte en el mejor programador ")
print("hola bienvenido al mundo codemon")
input()
print("mi nombre es profesor Carlos")
print("pero todos me conocen como el profesor de programación")
input()
print("este mundo está habitado por criaturas llamadas codemon")
print("cada uno de ellos tiene habilidades únicas ")
input()
print("antes de comenzar.....")

nombre_jugador = input(" D i g a m e  C u a l   e s   s u   n o m b r e:      ")

print(f"mucho gusto, {nombre_jugador} ahora seguiré con la explicación")
input("")
print("Tu aventura está a punto de comenzar.")
print("Prepárate para aprender, crear y superar desafíos.")
input("")
print("Recuerda:")
print("Programar es comprender y corregir errores es crecer.")
input("")
print(f"{nombre_jugador} tu historia de codemon está a punto de comenzar ahora ")
input("")
print(f"{nombre_jugador} te acabas de levantar, bajas las escaleras y te encuentras con tu mamá")
input("")
print("tu mamá está triste porque te tienes que ir de casa ")
print("ella te dice que tienes que ir al laboratorio del profesor Carlos porque te quiere ver ")
input("")
print("vas caminando hacia el laboratorio del profesor Carlos   ")
print("de repente te encuentras con él 0o0")
input("")
print("él te dice que justo te estaba buscando")
print("él te guía hacia su laboratorio, llegan al laboratorio ")
input("")  
print("el profesor Carlos te comenta que como vas a iniciar tu viaje te quiere dar un codemon")
print("frente a ti aparecen 3 cápsulas cada una con un codemon distinto")
print()

charmander = {
    "nombre": "charmander",
    "vida": 100,
    "ataques": ["Arañazo", "Ascuas", "Gruñido"]
}

squirtle = {
    "nombre": "squirtle",
    "vida": 100,
    "ataques": ["pistola Agua", "Placaje", "Refugio"]
}

bulbasaur = {
    "nombre": "bulbasaur",
    "vida": 100,
    "ataques": ["Látigo Cepa", "Placaje", "Gruñido"]
}

pikachu = {
     "nombre": "pikachu",
    "vida": 100,
    "ataques": ["impactrueno", "rayo" , "ataque rapido"]

}

codemon_inicial = ["charmander" , "squirtle" , "bulbasaur" , "pikachu"]

for eleccion in range(len(codemon_inicial)):
    print(f"-- {codemon_inicial[eleccion]}")

while True:
    codemon_elegido = input("Q u e  C  o d e m o n  I n i c i a l   q u i e r e s   E l i g i r :      ").lower()

    if codemon_elegido == "charmander":
        codemon = charmander
        break
    elif codemon_elegido == "squirtle":
        codemon = squirtle
        break
    elif codemon_elegido == "bulbasaur":
        codemon = bulbasaur
        break
    elif codemon_elegido == "pikachu":
        codemon = pikachu
        break
    else:
        print("Opcion invalida")
        continue

print()
print("después de haber conseguido tu codemon te despides del profesor Carlos")
print("luego de salir del edificio te quedas un momento mirando el horizonte")
input("")
print("en él ves diferentes caminos y con ello diferentes desafíos ")

rutas = ["Ruta Hacia la Ciudad Código Fuente" , "Ruta Hacia la Ciudad Quantum Code" ,"Ruta Hacia la Ciudad Datagrama" , "Ruta Hacia la Ciudad Sinapsis "]

for i in range(len(rutas)):
      print(f"{i} -- {rutas[i]}")


while True:
    ruta_elegida = input("Elija la ruta que Quiera Recorrer (0/1/2/3):    ")
    if ruta_elegida == "0":
        print("después de pensarlo te atreves a ir a un camino que parece tranquilo")
        print("pero el camino también parece no tan fácil")
        print() 
        print("pero decides ir comenzando tu viaje de programador")
        break
    elif ruta_elegida == "1":
        print("después de pensarlo te atreves a ir a un camino que parece tranquilo")
        print("pero el camino también parece no tan fácil")
        print() 
        print("pero decides ir comenzando tu viaje de programador")
        break
    elif ruta_elegida == "2":
        print("después de pensarlo te atreves a ir a un camino que parece tranquilo")
        print("pero el camino también parece no tan fácil")
        print() 
        print("pero decides ir comenzando tu viaje de programador")
        break
    elif ruta_elegida == "3":
        print("después de pensarlo te atreves a ir a un camino que parece tranquilo")
        print("pero el camino también parece no tan fácil")
        print() 
        print("pero decides ir comenzando tu viaje de programador")
        break
    else:
        print("Opcion Invalida")
        continue



print()

print("vas caminando por la ruta, pero de repente aparece un programador con actitud confiada")
print("el programador se llama Hachimaki *-*")
print("sin más introducción te invita a un combate ")
print("tú aceptas pero el combate no era como pensabas...........")
input("") 


vida_de_codemon = 100
dragonite_entrenador = 150

import random

print("¡El Enfrentamiento da Comienzo!")
print()
print(f"Tu lanzas tu {codemon['nombre']} , mientras que Hachimaki saca su Dragonite")



while vida_de_codemon > 0 and dragonite_entrenador > 0:
       print("\n--- TU TURNO ---")
       print()
       print("Tus ataques son:")
       for i, ataque in enumerate(codemon["ataques"]):
         print(f"{i} -- {ataque}")

       ataque_propio = int(input("Elija que ataque va a Realizar (Seleccione el Numero del ataque) :    "))
    
       if ataque_propio == 0 :
            print(f"{codemon['nombre']} usó {codemon['ataques'][0]}")
            print()

            daño = random.randint(12, 20)

            critico = random.random() < 0.15

            if critico:
                daño *= 2
                print("¡Golpe crítico!")

            dragonite_entrenador -= daño
            print(f"Hiciste {daño} de daño. Vida del Codemon Dragonite: {dragonite_entrenador}")

       elif ataque_propio == 1 :
            print(f"{codemon['nombre']} usó {codemon['ataques'][1]}")

            daño = random.randint(9, 16)

            critico = random.random() < 0.2

            if critico:
                daño *= 2
                print("¡Golpe crítico!")

            dragonite_entrenador -= daño
            print(f"Hiciste {daño} de daño. Vida del Codemon Dragonite: {dragonite_entrenador}")
       elif ataque_propio == 2 :
            print(f"{codemon['nombre']} usó {codemon['ataques'][2]}")

            daño = random.randint(10, 20)

            critico = random.random() < 0.1

            if critico:
                daño *= 2
                print("¡Golpe crítico!")

            dragonite_entrenador -= daño
            print(f"Hiciste {daño} de daño. Vida del Codemon Dragonite: {dragonite_entrenador}")
            
       else:
            print("Opción inválida")
            continue
        


       if dragonite_entrenador > 0:
            print("\n--- TURNO ENEMIGO ---")

            daño_enemigo = random.randint(20, 38)

            critico_enemigo = random.random() < 0.15
            if critico_enemigo:
                daño_enemigo *= 2
                print("¡El enemigo hizo un crítico!")

            vida_de_codemon -= daño_enemigo
            print(f"Dragonite hizo {daño_enemigo} de daño. Tu vida restante es: {vida_de_codemon}")

       if vida_de_codemon<= 0:
            print("\n Has perdido...")
       elif dragonite_entrenador <= 0:
            print("\n ¡Ganaste el combate!")  



print("a pesar de que lo intentaste terminaste perdiendo")
input("") 
print("después de la batalla, Hachimaki no se burla de ti ni se va sin más ")
print("él te da unas palabras: no basta con querer ganar, tienes que entender a tu codemon")
print("confiar y aprender de tus errores ")
input("") 
print("estas palabras te quedan dando vueltas.")
input("") 
print("después de recuperarte sigues avanzando y finalmente llegas a una ciudad")
print("el ambiente es distinto: gente caminando, tiendas abiertas, programadores por todos lados")
input("") 
print("empiezas a hacer cosas cotidianas ")
print("buscas un lugar para quedarte, compras en algunas tiendas, compras algunas cosas básicas")
input("") 
print("mientras caminas divisas un gimnasio pero decides ir después ")
print("primero quieres entrenar para ser el mejor programador")
input()
print(" Al  Dia  Siguiente ...")
input("") 
print("decides ir al gimnasio codemon ")
input("") 
print("el ambiente es muy serio y desafiante")
print("ahí conoces al líder de gimnasio, que tiene una vibra fuerte y segura")
print("este no pelea de inmediato ")
input("") 
print("él te dice que si quieres combatir tienes que demostrar que estás preparado")
input("")
print("Por eso te dice de tener un combate de prueba para verificar si tienes lo necesario  ")
print("Para enfrentarte a el en un combate real , por la medalla de gimnasio ")
input()



print(" ¡El Emfrentamiento de Prueba con el lider de Gimnasio va a Comezar! ")
input()



import random

vida_jugador = 150

nombre_lider = "Lider de Gimnasio"
vida_lider = 200

turno = 1

print("\n===================================")
print(f"{nombre_jugador} vs {nombre_lider}")
print("¡Comienza el combate!")
print("===================================")



print(f"Tu lanzas tu {codemon['nombre']} , mientras que el {nombre_lider} lanza su Geodude")

while vida_jugador > 0 and vida_lider > 0:

     print(f"\n===== TURNO N°{turno} =====")

     print("\nTu Turno:")
     print(f"Tu vida: {vida_jugador}")
     print(f"Vida del {nombre_lider}: {vida_lider}")

     for i, ataque in enumerate(codemon["ataques"]):
         print(f"{i} -- {ataque}") 
    
    
     enfrentamiento_lider = int(input("Elija que ataque va a Realizar (Seleccione el Numero del ataque) :    "))

     daño = 0

     if enfrentamiento_lider == 0 :
         print(f"{codemon['nombre']} usó {codemon['ataques'][0]}")
         daño = random.randint(14, 35)

     elif enfrentamiento_lider == 1 :
         print(f"{codemon['nombre']} usó {codemon['ataques'][1]}")
         daño = random.randint(12, 30)
 
     elif enfrentamiento_lider == 2 :
         print(f"{codemon['nombre']} usó {codemon['ataques'][2]}")
         if random.randint(1, 100) <= 30:
            print("Fallaste el ataque")
         else:
            daño = random.randint(15, 35)

     else:
        print("Opción inválida, pierdes turno")


     if daño > 0 and random.randint(1, 100) <= 20:
         daño *= 2
         print("¡Golpe crítico!")


     vida_lider -= daño
     print(f"Hiciste {daño} de daño , Vida restante del {nombre_lider}:  {vida_lider}")
  
  

     input("\nPresiona ENTER para continuar...")

     print("\nTurno del líder de Gimnasio")
     
     if vida_lider < 30:
        print("Geodude Uso Defensa Ferrea")
        vida_lider += 25
        print(" Esto ase que Geodude obtenga 25 puntos de vida , como si fuese un escudo extra")
        vida_lider += 25
        print()
        print(f"La vida Restante del {nombre_lider} es :  {vida_lider}")
     elif vida_jugador >= 75:
        print("Geodude uso Placaje")
        daño = random.randint(10, 22)

     else:
        print("Geodude uso Lanzarrocas")
        daño = random.randint(12,24)
         

     if random.randint(1, 100) <= 20:
         daño *= 2
         print("¡Golpe crítico enemigo!")
 
     vida_jugador -= daño
     print(f"El {nombre_lider} te hizo {daño} de daño")
     print()
     print(f"Tu Vida Restante es : {vida_jugador}")

     turno += 1

     input("\nPresiona ENTER para el siguiente turno...")

     
print("========================================================="*2)
print("========================================================="*2)
if vida_jugador < 0 :
     print("Perdiste ...")
     print("El lider se dirige hacia donde estas y te dice que tienes talento solo que te falta practica y que te estara esperando ")
     print("para un Proximo duelo ")
elif vida_lider < 0 :
     print(" !Ganaste el Combate!")
     print("El lider se dirige hacia donde estas y te dice que estas bastante capacitado para que tengan un emfrentamiento ")
     print("Y te Cita a que vengas a enfrentarlo en unos dias mas ")
print("========================================================="*2)
print("========================================================="*2)



input()
print("luego de salir del gimnasio te encuentras que hay muchos programadores hablando")
print("de un programador misterioso que está desafiando a todos")
input("") 
print("decides encontrarte con él .......")
input("") 
print("Al  llegar al lugar que escuchaste que se encontraba ")
input()
print("Lo encuentras al final de un combate , el cual observas como termina ganando este entrenador misterioso ")
input()
print("El entrenador te ve con cara de como si estuvieses interesado y decide retarte  ")
input()


combate_entrenador_misterioso = input("Quieres enfrentarte al Entrenador Misterioso o prefieres rechazarlo (si/no):    ").lower()

vida_alakazam = 120
vida_de_tu_codemon= 150


import random



if combate_entrenador_misterioso == "si":
    print()
    
    print("###"*15)
    print("  ¡ ¡ Q u e   C o m i e n z e   e l   C o m b a t  e   ! ! ")
    print("###"*15)
    print()
    print("Este entrenador tiene a Alakazam un codemon tipo psiquico , con una inteligencia extrema y poderes mentales  ")

    while vida_de_tu_codemon > 0 and vida_alakazam > 0:
        print()
        print("===== TU TURNO ======")
        print()
        print("Tus ataques son :")
        
        for i, ataque in enumerate(codemon["ataques"]):
             print(f"{i} -- {ataque}")
        

        propio_ataque = int(input("Elija que ataque va a Realizar (Seleccione el Numero del ataque) :    "))

        if propio_ataque == 0 :
             print(f"{codemon['nombre']} usó {codemon['ataques'][0]}")
             daño = random.randint(15,30)

             criticos = random.random() < 0.20
             if criticos:
                daño *= 2
                print("¡¡ AS Realizado un Golpe Critico!!")

                vida_alakazam -= daño
             print()
             print(f"Hiciste {daño} de Daño al enemigo ,  La vida restante de tu enemigo es {vida_alakazam}")
        elif propio_ataque == 1 :
             print(f"{codemon['nombre']} usó {codemon['ataques'][1]}")
             daño = random.randint(10,28)

             criticos = random.random() < 0.25
             if criticos:
                daño *= 2
                print("¡¡ AS Realizado un Golpe Critico!!")

                vida_alakazam -= daño
             print()
             print(f"Hiciste {daño} de Daño al enemigo ,  La vida restante de tu enemigo es {vida_alakazam}")
        elif propio_ataque == 2 :
             print(f"{codemon['nombre']} usó {codemon['ataques'][2]}")
             daño = random.randint(18,40)

             criticos = random.random() < 0.15
             if criticos:
                daño *= 2
                print("¡¡ AS Realizado un Golpe Critico!!")

                vida_alakazam -= daño
             print()
             print(f"Hiciste {daño} de Daño al enemigo ,  La vida restante de tu enemigo es {vida_alakazam}")
        else:
            print("Ataque Invalido")
            continue



        if vida_alakazam > 0:
            print("\n--- TURNO ENEMIGO ---")
            print()
            

            if vida_de_tu_codemon > 90:
             print("Alakazam utilizo Ataque Psiquico ")
                
             daño_enemigo = random.randint(14, 28)

             critico_enemigo = random.random() < 0.18
            
            
             if critico_enemigo:
                 daño_enemigo *= 2
                 print("¡El enemigo hizo un crítico!")
                 vida_de_tu_codemon -= daño_enemigo
                 print()
             print(f"Has recibido {daño_enemigo} de daño Enemigo , tu vida Restante es {vida_de_tu_codemon}")
            elif vida_de_tu_codemon < 90:
                 print()
                 print("Alakazam  utilizo  Confucion ")

                 daño_enemigo = random.randint(10, 25)

                 critico_enemigo = random.random() < 0.22
                 if critico_enemigo:
                     daño_enemigo *= 2
                     print("¡El enemigo hizo un crítico!")
                     vida_de_tu_codemon -= daño_enemigo
                     print()
                 print(f"Has recibido {daño_enemigo} de daño Enemigo , tu vida Restante es {vida_de_tu_codemon}")
            elif vida_alakazam < 30:
                print()
                print("Alakazam a Utilizado Recuperacion")
                print()
                print("Alakazam se a Recuperado 30 de vida ")

                vida_alakazam += 30
                print(f"La vida de Alakazam es {vida_alakazam}")
            

            if vida_alakazam < 0:
                print("¡¡Ganaste!!")
            elif vida_de_tu_codemon < 0:
                print("Pediste ...")
elif combate_entrenador_misterioso == "no":
    print()
    print("No gracias solo estoy observando ( Decides no cambatir ya que te sientes cansado despues del combate con el Lider del gimnasio)")
else:
    print("Escriba una opcion Valida")




print("luego de tu travesía vas a la ciudad pero hay algo raro")
input()
print("hay un codemon suelto y está fuera de control!")
print("decides intentar calmarlo pero este no colabora")
input()
print("Asta casi te hace daño pero te lograste salvar")
input()
print("entonces ves que no hay otra forma de calmarlo que venciendo en una batalla de codemon ")
input()


print(f"Decides sacar tu {codemon['nombre']} , antes de que el codemon fuera de control te ataque a tu primero ")
input()
print(" decides Atacar tu primero ")


import random

vida_del_jugador = 150
vida_enemigo = 85

print("\n===================================")
print("   EVENTO CODEMON FUERA DE CONTROL   ")
print(" ===================================  ")

print("-----------------------------"*2)
print("  Comienza El Combate VS Codemon Fuera de Control ")
print("-----------------------------"*2)




while vida_del_jugador > 0 and vida_enemigo > 0:
     print()
     print("===== TU TURNO ======")
     print()

     print(" Tus  Ataques  Son : ")

     for i, ataque in enumerate(codemon["ataques"]):
         print(f"{i} -- {ataque}")

     codemon_fuera_control = int(input("Elija que ataque va a Realizar (Seleccione el Numero del ataque) :    "))

     if codemon_fuera_control == 0 :
         print(f"{codemon['nombre']} usó {codemon['ataques'][0]}")
         print()
         daño = random.randint(10, 25)

         if random.random() < 0.2:
             daño *= 2
             print(" ¡Golpe crítico! ")

         vida_enemigo -= daño
         print(f"Atacas haciendo {daño} de daño , vida del codemon : {vida_enemigo}")
     elif codemon_fuera_control == 1 :
         print(f"{codemon['nombre']} usó {codemon['ataques'][1]}")
        
         daño = random.randint(10, 22)

         if random.random() < 0.15:
            daño *= 2
            print(" ¡Golpe crítico! ")
        
         vida_enemigo -= daño
         print(f"Atacas haciendo {daño} de daño , vida del codemon : {vida_enemigo}")
     elif codemon_fuera_control == 2 :
         print(f"{codemon['nombre']} usó {codemon['ataques'][2]}")
         daño = random.randint(10,24)
        
         if random.random() < 0.18:
             daño *= 2
             print(" ¡Golpe crítico! ")

         vida_enemigo -= daño
         print(f"Atacas haciendo {daño} de daño , vida del codemon : {vida_enemigo}")

     else:
         print(" ¡Opción inválida! ")




     if vida_enemigo > 0:
         print()
         print(" ¡El Codemon Fuera de Control Va a Contraatacar! ")
         print("\n--- TURNO ENEMIGO ---")
         print()
    
         daño_enemigo = random.randint(10, 18)

         if random.random() < 0.15:
             daño_enemigo *= 2
             print("Ataque crítico del enemigo")

         vida_del_jugador -= daño_enemigo
         print(f"El Codemon Enemigo te iso {daño_enemigo} , Vida Restante: {vida_del_jugador}")





print("========================================================="*2)
print("========================================================="*2)
if vida_del_jugador <= 0:
    print("As Perdido ... , el Codemon fuera de control sigue haciendo caos  ")
elif vida_enemigo <= 0 :
    print(" ¡Feliciadades Detuviste al Codemon fuera de control!  ")
print("========================================================="*2)
print("========================================================="*2)







print()
print("Luego de ese evento que tuviste decideste irte a descansar ")
input()
print(" 3 Dias Despues . . .")
input()
print("Pasaron Unos 3 dias desde ese ultimo evento , no te detuviste")
input()
print("Estuviste entrenando , reflexionando y recapacitando de tus errores   ")
input()
print("Que as tenido a lo largo de tu camino  ")
input()
print("En ese mismo dia decidiste descansar esa tarde tan tranquila era perfecta para un descanso")
input()
print("O eso era lo que creias . . .")
input()




print("Cuando estabas a mitad de camino a un lugar tranquilo  ")
input()
print("Que te mencionaron en la ciudad  , cuando recien la estavas explorando ")
input()
print(" Sin darte cuenta , Sentiste una presencia Fuera de lo Habitual a tus espaldas ")
input()
print("Decidiste darte la vuelta  ")
input()
print("No habia nadie ")
input()
print("Pensaste que te habias equivocado  , asta que ves caer unas hojas en frente tuyo y")
input()
print("Miras al cielo y presencias como   ")
input()
print("El cielo se enfría de repente . . aparece volando lentamente . . te observa… y se va sin atacar ")
input()
print("Era articuno , un Codemon Legendario que solo habias visto en libros y que ahora estaba")
input()
print("Pasando lentamente por arriba tuyo ")
input()
print("Observas sorprendido como vuela tan silenciosamente , con un vuelo tan elegante que te deja sin palabras ")
input()
print("Y sin darte cuenta lo ves desaparecer en las nubes ")
input()

print("El silencio vuelve . . . pero algo en ti ya no es igual")
input()
print("No sabes por qué, pero sientes que ese encuentro significó algo")
input()
print("Como si no hubiera sido casualidad")
input()

print(f"Después de todo eso, {nombre_jugador}, te desconectas de todo el ruido de la ciudad.")
input()
print("Decides sentarte en un lugar alejado y miras hacia el horizonte.")
input()
print("El cielo ya no se ve igual desde que viste a Articuno")
input()
print("Y piensas en todo lo que has pasado. Has cometido errores, pero de ellos aprendiste.")
input()
print("Recuerdas las sabias palabras de Hachimaki.")
input()
print("Y te dices a ti mismo:")
input()
print("Esto no fue el final . . .")
input()
print("Esto fue solo el comienzo de mi aventura como Programador")
input()

print(r"""
███████╗██╗███╗   ██╗
██╔════╝██║████╗  ██║
█████╗  ██║██╔██╗ ██║
██╔══╝  ██║██║╚██╗██║
██║     ██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═══╝
""")
