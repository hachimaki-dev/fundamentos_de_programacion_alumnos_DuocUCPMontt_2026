#importar librería "random" para poder aleatorizar variables numéricas
import random


clase_usuario = ""
clase_guerrero = "guerrero"
clase_ladron = "ladrón"
numero_puerta = 0
puerta_abierta = False
opcion_usuario = ""
intentos = 0
buscar_llave = "Buscar la llave"
forzar_puerta = "Forzar la puerta"
Usar_ganzua = "Usar una ganzúa"
factor_50 = random.randint(1,10)
puertas_abiertas = 0
intentos = 0


print("Escape del calabozo de las 3 puertas")
clase_usuario =input("Elija una clase:"
" guerrero o ladrón " )
#El for limita la cantidad de puertas a 3 puertas, repitiendose el proceso 3 veces
for numero_puerta in range(1,4):
    factor_50 = random.randint(1,10)
    #si los intentos superan los 3 por habitación, pierde
    while intentos < 3 and puertas_abiertas < 3:

        opcion_usuario = input(f"""El {clase_usuario} se encuentra atrapado en una habitación ¿Qué debería hacer?
                               (1) Buscar la llave
                               (2) Forzar la puerta
                               (3) Usar una ganzúa""")
        if opcion_usuario == buscar_llave:
            factor_50 = factor_50 % 2
            if factor_50 != 0:
                print(f"El {clase_usuario} encontró la llave y abrió la puerta")
                puertas_abiertas = puertas_abiertas +1
            else:
                intentos = intentos +1
                print(f"El {clase_usuario} Intentó buscar la llave pero no hayó nada... ¿Que debería hacer?")
        elif opcion_usuario == forzar_puerta:
            if clase_usuario == clase_guerrero:
                print("El guerrero usa su fuerza y logra abrir la puerta")
                puertas_abiertas = puertas_abiertas +1
            elif clase_usuario == clase_ladron:
                intentos = intentos +1
                print(f"El ladrón intenta forzar la puerta pero no lo logra ¿Qué debería hacer? y va en el intento n {intentos}")
        elif opcion_usuario == Usar_ganzua:
            if clase_usuario == clase_ladron:
                print("El ladrón usa una ganzua y abre la puerta")
                puertas_abiertas = puertas_abiertas +1
            elif clase_usuario == clase_guerrero:
                intentos = intentos +1
                print("El guerrero rompe la ganzúa y no logra abrir la puerta... ¿Qué debería hacer?")


if intentos == 3:
    print(f"El {clase_usuario} se queda en un rincón encerrado en la puerta {numero_puerta} 3")
else:
    print(f"El {clase_usuario} Logra escapar de las 3 habitaciones del calabozo")