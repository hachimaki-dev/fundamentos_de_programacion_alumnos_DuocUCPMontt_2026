numero_secreto = 5
esta_jugando = True
numero_elegido_por_usuario = 0  

input("Bienvenido a adivina el número tienes que tratar de adivinar el número oculto entre el 1 y el 10 presiona ENTER para jugar")

while esta_jugando :
    numero_elegido_por_usuario = int(input(f"Adivina cual es el número secreto: "))
    if numero_elegido_por_usuario == numero_secreto :
        esta_jugando = False
        print(f"FELICIDADES ADIVINASTE LOKO KAPO ERA {numero_elegido_por_usuario}")
    
    else : 
        print(f"No es {numero_elegido_por_usuario} sigue intentando")

