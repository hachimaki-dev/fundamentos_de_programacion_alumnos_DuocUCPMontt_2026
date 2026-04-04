print ("======================================")
print ("===Bienvenido a la escusta colegial===")
print ("======================================\n")

import time
import sys

print ("En esta escuesta votaran para que una directiva se quede o no.")
print ("Así que por favor voten con claridad y siendos conscientes de ello.\n")

print ("Para votar solo deben de ingresar si estan estan a 'favor (A) o en Contra (C)'. ")
print ("Por si no esta claro, Aquí abajo una pequeña seccíon de como debe de ser la votacíón.\n")

print ("1. Votación a Favor, para votar a Favor debes de ingresar una 'A'.")
print ("2. Votación en Contra, para votar en contra debes de ingresar una 'C'.'\n")

print ("Con todo esto dicho, en la seccíon de abajo podran ingresesar cuantos van a votar.")
print ("¿Cuántos estudiantes van a votar.\n")

Numero_de_escuestados = int(input("Ingrese el número de estudiantes : "))
contador_de_votos_a_favor = 0
contador_de_votos_en_contra = 0
contador_votos_invalidos = 0


while Numero_de_escuestados > 0 :
    voto_de_estudainte = str(input("Ingrese su voto : ")).lower()

    if voto_de_estudainte == "a":
        print ("Bien, hecho tu voto.")
        contador_de_votos_a_favor += 1
        Numero_de_escuestados -= 1
        print (f"Estudiantes faltantes {Numero_de_escuestados}")

    elif voto_de_estudainte == "c":
        print ("Bien, has hecho tu voto")
        contador_de_votos_en_contra += 1
        Numero_de_escuestados -= 1
        print (f"Estudiantes faltantes {Numero_de_escuestados}")

    else:
        print ("Voto invalido, por favor ingrese 'A' o 'C'.")
        contador_votos_invalidos += 1
        print (f"Van {contador_votos_invalidos} votos invalidos.")

print ("Todos los estudiantes han hecho sus votos.")
print ("Ahora estamos contando cada uno de ellos para dar con el ganador.")
print ("Espere pacientemente.\n")
time.sleep(5)        

if contador_de_votos_a_favor > contador_de_votos_en_contra :
    print (f"Gana los votos 'a favor' con una cantidad de {contador_de_votos_a_favor} votos.")
    print ("Ahora un resumen de los votos.\n")

    print (f"{contador_de_votos_a_favor} votos a favor, {contador_de_votos_en_contra} votos en contra y {contador_votos_invalidos} invalidos.")

elif contador_de_votos_a_favor < contador_de_votos_en_contra :
    print (f"Ganan los votos 'en contra' con una cantidad de {contador_de_votos_en_contra} votos.")
    print ("Resumen de los votos.\n")

    print (f"{contador_de_votos_en_contra} votos en contra, {contador_de_votos_a_favor} votos a favor y {contador_votos_invalidos} invalidos.")

elif contador_de_votos_a_favor == contador_de_votos_en_contra :
    print ("Empate, los votos se igualaron en la misma cantidad.")
    print ("Resumen de los votos. \n")

    print (f"{contador_de_votos_en_contra} votos en contra, {contador_de_votos_a_favor} votos a favor y {contador_votos_invalidos} invalidos.")







    
    
    



