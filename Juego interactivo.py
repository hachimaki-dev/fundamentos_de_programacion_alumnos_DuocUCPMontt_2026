#imports para hacer funcionar diversas funciones del sistema dentro del programa de python
#en este caso time es importante para que el sistema se tome su tiempo mostrando cada una de las oraciones y os,subprocess para la funcion de limpiar la terminal

import sys
import subprocess
import time
import os

#def permite crear funciones, shotout al compañerx que puso en la rama main su novela ashdhads
def limpiar_term():
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=True)
    else:
        subprocess.run("clear", shell=True, check=True)


limpiar_term()
print("""
█▀█ █▀█ █▄▀ █▀▀ █▀▄▀█ █▀█ █▄░█   █▀▀ █░░ █   █▀▀ █▀▄ █ ▀█▀ █ █▀█ █▄░█
█▀▀ █▄█ █░█ ██▄ █░▀░█ █▄█ █░▀█   █▄▄ █▄▄ █   ██▄ █▄▀ █ ░█░ █ █▄█ █░▀█
""")
print("Pokémon Edición CLI abridged")

time.sleep(2)

print ("\nHola, Bienvenido al Mundo Pokémon.")
time.sleep(1)
print ("\nMi nombre es Profesor Oak, y soy un profesor que se dedica al estudio de estas creaturas llamadas Pokémon.")
time.sleep(1)
print("""
⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⣿⣧⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⢸⣿⣿
⣿⣿⡄⠘⣷⣤⡉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣥⣶⠇⢠⣿⣿⣿
⣿⣿⣿⣦⠈⠻⣿⣷⣄⠻⡿⠋⠙⠉⠋⠛⢿⡟⢡⣶⣿⡿⠃⣰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣈⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠐⢿⠿⢋⣤⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⡤⠄⠀⠀⠀⢀⠤⡀⢰⣿⡿⠛⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡾⠀⠀⠀⢸⣶⡇⢸⠟⠁⠀⠈⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠁⠤⠬⠤⠄⠉⠀⢀⠀⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢟⣵⢄⣀⡀⠀⠀⣀⣠⣰⣿⡶⣆⡄⣀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣟⣾⡏⣿⣿⣿⣿⣿⣿⣿⡷⣿⣯⣿⣿⣿⣇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣤⡈⢷⢹⣿⣿⣿⣿⣿⣿⠁⡿⢟⣿⣿⣿⣹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠁⠉⠻⣿⣿⠟⠀⠘⢸⣿⣿⡿⣡⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠘⠀⠀⠀⢠⣭⣭⣵⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠓⠒⠛⠓⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋
""")
time.sleep(3)
limpiar_term()

Creacion= False
while Creacion==False:
    print("\nAhora cuentame un poco sobre ti")

    Genero =input("\n¿Eres un Chico, una Chica o prefieres otro termino?: ")

    Nombre =input("\nMuy Bien, ahora cuentame ¿Cómo te llamas?: ")

    print(f"\nMuy bien asi que eres {Genero} y te llamas {Nombre}")

    Confirmacion = False
    

    while Confirmacion== False:
        Correcion = input("es esto correcto? (Opciones Y/N) ")
        if Correcion == "Y":
            Creacion=True
            Confirmacion=True
    
        elif Correcion == "N":
            limpiar_term()
            print("Dejame preguntarte de nuevo entonces")
            Creacion=False
            Confirmacion=True
    
        else: 
            print("Opcion Invalida")
            Confirmacion = False

limpiar_term()    
Rival = False

while Rival ==False: 
    print("\nEste es mi nieto,ustedes han sido amigos toda la vida pero siempre se me olvida su nombre (que terrible abuelo soy)")
    print(f"\n{Nombre} ¿puedes decirme como se llamaba mi nieto?")
    NombreRival=input("\nIngresa el nombre de tu rival ")
    
    print(f"\n¿Se llamaba {NombreRival}?")
    Confirmacion2 = False
    

    while Confirmacion2== False:
        Correcion = input("es esto correcto? (Opciones Y/N) ")
        if Correcion == "Y":
            Rival=True
            Confirmacion2=True
    
        elif Correcion == "N":
            limpiar_term()
            print("Dejame preguntarte de nuevo entonces")
            Rival=False
            Confirmacion2=True
    
        else: 
            print("Opcion Invalida")
            Confirmacion2 = False

limpiar_term()
print(f'Okay {Nombre} Tu aventura en el Mundo Pokémon esta por comenzar, te espero en mi laboratorio')
time.sleep (2)
limpiar_term()

print ("Te despiertas en Pueblo paleta y te diriges al laboratorio del Profesor Oak")

print (f"\nProfesor Oak: Oh! {Nombre}, por fin estas aqui tengo un grupo de Pokémon recien capturados que quiero entregarles a ti y a {NombreRival} para que que entrenen y se conviertan en Maestros Pokémon")
time.sleep (1)
print (f"\n{NombreRival}: Vamos Abuelo, ¿realmente le tienes que dar un Pokémon a {Nombre}?, ¿porque no solo a mi me das los tres ya que yo soy el mejor entrenador despues de todo?")
time.sleep (1)
print (f"\nProfesor Oak: JAJAJAJA, tan arrogante como siempre {NombreRival}, por tu impaciencia y arrogancia ya he decidido que le voy a dar a {Nombre} a elegir primero")
time.sleep (1)
print (f"\nProfesor Oak: ¡Vamos {Nombre}!, Elije entre estas 3 opciones")

PokemonInicial = int(input("""Escoje entre las siguientes opciones:
1) Bulbasaur
2) Squirtle
3) Charmander

Introduce un numero: """))

if PokemonInicial == 1:
    print("Has escogido a Bulbasaur")
    Pokemon1= "Bulbasaur"
elif PokemonInicial == 2:
    print  ("Has escogido a Squirtle")
    Pokemon1= "Squirtle"
elif PokemonInicial == 3:
    print ("Has escogido a Charmander")
    Pokemon1= "Charmander"
elif PokemonInicial == 25:
    print ("HAS DESCUBIERTO UN EASTER EGG \n Has escogido a Pikachu")
    Pokemon1= "Pikachu"
else :
    print ("Opcion Invalida")
