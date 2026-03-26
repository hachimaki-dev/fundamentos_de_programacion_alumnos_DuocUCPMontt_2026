
import os 
os.system("cls" if os.name == "nt" else "clear")

while True :
    
    print("\n" + "="*20)
    print("¡BIENVENIDO AL MENÚ DE LA COMIDITA, SELECCIONE EL PLATO QUE MAS LE GUSTE Y DISFRUTE!\n")
    print("1. Papa rellena")
    print("2. Cazuela")
    print("3. Pollo arvejado")
    print("4. Salir")
    print("\n" + "="*20)

    selección_comida = int(input("Eliga una comida del menú"))

    if selección_comida == 1 :
        print("¡Elegiste la papa rellena!")
        print("Este plato trae lo siguiente: Masa frita de papa cocida, rellena de carne de vacuno, pollo, queso, cebollas, aceitunas, huevos duros, entre otros ingredientes picados.")
        break
    elif selección_comida == 2 :
        print("¡Elegiste la cazuela!")
        print("Este plato trae lo siguiente : Una presa de carne de vacuno, más verduras variadas: zapallo, choclo, papa.")
        break
    elif selección_comida == 3 :
        print("¡Elegiste el pollo arvejado!")
        print("Este plato trae lo siguiente:Pollo, pimenton verde y rojo, ajo, cebolla, zanahoria, arvejas, pimienta negra molida.")
        break
    elif selección_comida == 4 :
        print("Salir")
        break
    else :
        print("\n¡OPCIÓN NO VÁLIDA, VOLVER AL MENÚ!")
        