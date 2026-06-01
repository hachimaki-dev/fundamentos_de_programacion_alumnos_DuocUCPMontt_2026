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


id_del_animal = []

while True:
        try :
            cantidad_animales = int(input("ingresa la cantidad de animales: "))
            if cantidad_animales > 0:
                break
            else:
                print("ingresa un numero mayor que 0")
        except:
            print("ingresa un valor mayor que 0 y que sea un numero valido")


for cada_animal in range(cantidad_animales):
    while True:
        try: 
            nombre_animal = input(f"ingresa el id del animal {cada_animal +1}  minimo 6 caracters sin espacios: ").upper()
            if len(nombre_animal) >=6 and  " " not in nombre_animal:
                
                break
            else:
                print(" ingresa el id respetando las parametros dados")
            
        except:
                print("ingresa un numero mayor que 0 y real")
    id_del_animal.append(nombre_animal)

paciente_grande = 0
paciente_pequeno = 0

for cantidad_clasificacion in range(len(id_del_animal)):
    while True:
        try:
            peso_cada_animal = int(input(f"ingrese el peso del animal {cantidad_clasificacion+1} : "))
            if peso_cada_animal > 0:
                if peso_cada_animal >25:
                     paciente_grande +=1
                     break

                elif peso_cada_animal <= 25:
                     paciente_pequeno +=1
                     break
                
                else:
                     print("ingresa la cantidad de peso realista")
        except:
             print("ingrese un numero valido ")

print(f"La clínica ha registrado {paciente_grande} pacientes grandes y {paciente_pequeno} pacientes pequeños. ¡Bienvenidos!")


