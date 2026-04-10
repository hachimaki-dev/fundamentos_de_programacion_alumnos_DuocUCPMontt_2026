#1. Usa un ciclo para las 3 habitaciones (for i in range(1, 4)).
#2. En cada habitación, hay una puerta cerrada. El jugador debe elegir: 'Forzar', 'Ganzúa' o 'Buscar Llave'.
#3. Lógica de la habitación:
#- Si elige 'Buscar Llave', hay un 50% de probabilidad (puedes simularlo pidiendo un número y viendo si es par) de encontrarla. Si la tiene, puede abrir.
#- Si elige 'Ganzúa', debe tener la habilidad (pregunta al inicio del juego si es Ladrón o Guerrero). Solo el Ladrón abre con ganzúa.
#- Si elige 'Forzar', debe ser Guerrero.
#4. Si el jugador no logra abrir la puerta tras 3 intentos fallidos por habitación (ciclo while interno), pierde el juego completo.

intentos = 3
es_ladron = True
numero_llave_ingresado = 0
escapado = False
escoja_su_clase = int(input("Escoja su clase. 1:Guerrero  2:Ladron :"))
if escoja_su_clase == 2:
    es_ladron = True
elif escoja_su_clase == 1:
    es_ladron = False
print("Tu espiritu aventurero de lleva a un calabozo del cual ningun alma ha escapado")
print("Entras a la mazmorra")
for i in range(1, 4):
    
    while intentos > 0:
        eleccion = int(input("hay una puerta cerrada que haces? 1:Buscas una llave 2:Pruebas usar una ganzua 3:La fuerzas :"))
        numero_llave_ingresado = int(input("ingrese un numero del 1 al 20 :"))
        par_o_impar = numero_llave_ingresado % 2
        if par_o_impar == 0:
            numero_llave_ingresado_es_par = True
        else:
            numero_llave_ingresado_es_par = False
        if eleccion == 1 and numero_llave_ingresado_es_par == True:
            
            print("Que suerte! Encontraste una llave")
            print(f"entras a el cuarto numero {i}")
            break            
        elif eleccion == 2 and es_ladron == True:
            print("Tus habilidades de Ladron te deja abrir la puerta con tu ganzua")
            print(f"entras a el cuarto numero {i}")
            break
        elif eleccion == 3 and es_ladron == False:
            print("Tu fuerza de guerrero de deja forzar la puerta")
            print(f"entras a el cuarto numero {i}")
            break
        else:
            print("No pudiste abrir la puerta")
            print("el tiempo se te acaba")
            intentos -= 1

print("La puerta se cierra detras de ti")
if intentos > 0:
    print("Haz escapado.")
    print("Vives para morir otro dia")
else: 
    print("Una montaña de gusanos come-carne cae del tejado y te devora vivo")
    print("aqui acaba tu historia")