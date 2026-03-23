import time


water = 0
while water <= 4:
    water = water + 1
    print(f"llevamos {water}")
    if water == 3:
        break
    
    
algo = True

while algo == True:
    print("1. saludar")
    print("2. insultar")
    print("3. golpear")
    print("4. escupir")
    print("5. salir")
    respuestas = int(input("1 al 5  "))
    if respuestas == 1:
        time.sleep(2)
        print()
        time.sleep(2)
    elif respuestas == 2:
        time.sleep(2)
        print()
        time.sleep(2)
    elif respuestas == 3:
        time.sleep(2)
        print()
        time.sleep(2)
    elif respuestas == 4:
        time.sleep(2)
        print()
        time.sleep(2)
    elif respuestas == 5:
        algo = False
        print("Fin del programa")
        
