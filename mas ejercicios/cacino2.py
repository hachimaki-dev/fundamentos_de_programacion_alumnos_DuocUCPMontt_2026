"black jack:"
import random
joker = 1 or 11
cartas = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,10 , 11, 12, 13, joker]
suma = 0 

print("bienvenido al black jack")


jugar = input("deseas jugar ?: ")
while jugar == "s": 
    print("comenzemos:")
    print(" carta 1:")
    carta1 = print(random.randint(joker,cartas))
    carta2 = print(random.randint(1,13))
    suma = carta1 + carta2 
    print(f"tienes un todal de: {suma}")
    
