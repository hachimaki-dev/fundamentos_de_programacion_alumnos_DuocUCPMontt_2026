""" Ejercicio 22 — Sistema completo de gestión de una clínica veterinaria
Parte A (similar al Ejercicio 1 de evaluación):

Una clínica veterinaria registra a los animales que ingresan. El sistema debe:

Preguntar cuántos animales se registrarán (entero positivo, validado)
Para cada animal:
ID del animal: mínimo 6 caracteres, sin espacios (ej: GATO01, PERR7X, CONEJO2)
Peso en kg: entero positivo, validado
Clasificar:
Peso > 25 kg → Paciente Grande
Peso ≤ 25 kg → Paciente Pequeño
Al finalizar:
"La clínica ha registrado 3 pacientes grandes y 8 pacientes pequeños. 
¡Bienvenidos!"
"""
while True:
    try:
        ingreso_animales = int(input("cuantos animales se ingresaran : "))
        if ingreso_animales > 0 :
            break
        else:
            print("ingresa un numero mayor que 0")
    except:
        print("ingresa un numero valido")


id_animales = []

for id_por_cada_animal in range(ingreso_animales):
    while True:
            try:
                id_animal = input(f"ingrese el id del animal {id_por_cada_animal +1} minimo 6 caracters y sin espacios : ")
                if len(id_animal) >=6 and " " not in id_animal:
                    break
                else:
                    print("ingrese un nombre con los parametros dados")
            except:
                print("ingrese el nombre de manera correcta")
    id_animales.append(id_animal)

paciente_grande = 0
paciente_pequeno = 0

for cantidad_de_animales in range(len(id_animales)):
    while True:
        try:
            peso_animal = int(input(f"ingresa el peso del animal {cantidad_de_animales +1}: "))
            if peso_animal > 0:
                if peso_animal > 25:
                    paciente_grande+=1
                    break
                elif peso_animal <=25:
                    paciente_pequeno+=1
                    break
            else:
                print("ingresa un peso mayor que 0")
        except:
            print("ingresa un numero valido")

print(f"La clínica ha registrado {paciente_grande} pacientes grandes y {paciente_pequeno} pacientes pequeños. ¡Bienvenidos!")