### Minecraft - Menú de Crafteo
Espada_diamante = 1
Pico = 2
crafteos = 0

crafteo = int(input("Que vas a craftear? \n 1) Espada de Diamante \n 2) Pico \n 3) Salir de la Mesa de Crafteo "))
while True:
    if crafteo == 1:
        print("Espada de Diamante crafteada!")
        crafteos +=1
        crafteo = int(input("Que vas a craftear? \n 1) Espada de Diamante \n 2) Pico \n 3) Salir de la Mesa de Crafteo "))
    elif crafteo ==2:
        print("Pico listo!")
        crafteos +=1
        crafteo = int(input("Que vas a craftear? \n 1) Espada de Diamante \n 2) Pico \n 3) Salir de la Mesa de Crafteo "))
    elif crafteo ==3:
        print("Has salido de la mesa de crafteo.")
        break
    else:
        print("Escoja una receta que conozca.")
        continue

print(f"Has crafteado {crafteos} cosas.")