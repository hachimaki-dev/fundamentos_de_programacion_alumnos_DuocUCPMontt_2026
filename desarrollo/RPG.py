import time
import sys

print ("/============================/")
print ("/========Simulador RPG=======/")
print ("/============================/\n")


vida_de_usuario = 100
vida_del_jefe = 100
contador_de_mana = 70
ataque = 20
ataque_magia = 50
posicion_vida = 30
ataque_de_jefe = 15
coste_de_ataque = 1
coste_de_magia = 5
coste_de_salud = 30


print ("Deberas atacar a el jefe.")
print ("En caso de no matarlo este te va a quitar cierta cantidad de vida.\n")

print ("Pero unas intrucciones primero.")
print ("Espere pacientemente.\n")
print ("PROCESANDO...")
time.sleep(3)

print ("/=============================/")
print ("/========INTRUCCIONES=========/")
print ("/=============================/\n")

print ("1. Ataque basico (quita 20 de vida al jefe). Coste de maná --> (1)")
print ("2. Ataque de Magia (quita 50 de vida al jefe). Coste de maná --> (5) ")
print ("3. Poción de Vida (restaurara 30 de hp al usuario). Coste de maná -->(30).")
print ("4. Cuentas con 70 de maná.\n")

print ("Con todo esto dicho, es !HORA DE ACABAR CON EL JEFE¡")



while vida_de_usuario > 0 and vida_del_jefe > 0:
    eleccion_de_usuario = int(input("¿Qué ataque desea realizar? : "))
    print ("Recuerde seleccionar (1) , (2) o (3).")

    if eleccion_de_usuario == 1 :
        print ()
        print ("Usted ha elegido (Ataque basico).\n")
        vida_del_jefe = vida_del_jefe - ataque
        contador_de_mana = contador_de_mana - coste_de_ataque
        print (f"Le has quitado un total de ({vida_del_jefe}) HP.")
        print (f"Maná restante ({contador_de_mana}).")
        print ("Ahora a esperar el turno del jefe.\n")
        time.sleep(2)

        vida_de_usuario = vida_de_usuario - ataque_de_jefe
        print (f"OH NO, el jefe acaba de atacarte y te ha dejado con ({vida_de_usuario}) HP.\n")

    elif eleccion_de_usuario == 2:
        print ("Usted ha elegido (Ataque de magia).\n")
        vida_del_jefe = vida_del_jefe - ataque_magia
        contador_de_mana = contador_de_mana - coste_de_magia
        print (f"Excelente le has quitado un total de ({vida_del_jefe}) HP.")
        print (f"Maná restante ({contador_de_mana}).")
        print ("Ahora a esperar el turno del jefe.\n")
        time.sleep(2)
        vida_de_usuario = vida_de_usuario - ataque_de_jefe
        print (f"OH NO, el jefe acaba de atacarte y te ha dejado con ({vida_de_usuario}) HP.\n")

    elif eleccion_de_usuario == 3 :
        print (f"usted ha elegido (Poción de vida).")
        print ("Bien, es momento de curarnos.\n")
        contador_de_mana = contador_de_mana - coste_de_salud
        print ("REGENERANDO VIDA...\n")
        time.sleep(3)
        vida_de_usuario = vida_de_usuario + posicion_vida

        print ("Bien, te has regenerado, es momento de volver a la acción.")
        print (f"Tú salud ({vida_de_usuario}).")
        print (f"Maná restante ({contador_de_mana}).\n")

        print ("Esperando turno del jefe...\n")
        time.sleep(2)
        vida_de_usuario = vida_de_usuario - ataque_de_jefe
        print (f"OH NO, el jefe acaba de atacarte y te ha dejado con ({vida_de_usuario}) HP.\n")

        if vida_de_usuario < 50:
            print ("Oh no, el jefe te ha quitado la mitad del vida tu puedes.")

        elif vida_del_jefe <50 :
            print ("Bien, ya le hemos quitado la mitad de la vida, siga así.")

    else:
        print ("Ingrese solo (1) , (2) , (3).")

print ()
print ("Procesando calculos...")
time.sleep(5)
if vida_de_usuario == 0 :
    print ("Hemos perdido. :c")

elif vida_del_jefe == 0:
    print ("Hemos ganado, muy bien.")




    




