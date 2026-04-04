import time
import sys

Numero_de_escuestados = 0
contador_de_votos_a_favor = 0
contador_de_votos_en_contra = 0
contador_de_votos_no_validos = 0


while Numero_de_escuestados <= 30:
    voto_de_estudainte = str(input("Ingrese su voto : ")).lower()

    if voto_de_estudainte == "a":
        print ("Bien, hecho tu voto.")
        contador_de_votos_a_favor += 1
        Numero_de_escuestados -= 1
        print (f"Estudiantes faltantes {Numero_de_escuestados}")

    elif voto_de_estudainte == "c":
        print ("Bien, has hecho tu voto")
        contador_de_votos_en_contra += 1
        Numero_de_escuestados -= 0
        print (f"Estudiantes faltantes {Numero_de_escuestados}")


    else: 
        print ("Voto incontabilizado, por favor ingrese 'A' o 'C' ")
        contador_de_votos_no_validos += 1
        print (f"Van {contador_de_votos_no_validos} votos invalidos")
        


        




print ("Todos los estudiantes han hecho sus vots.")
print ("Por favor esperen que estamos valinado cada uno de ellos")
time.sleep(5)


