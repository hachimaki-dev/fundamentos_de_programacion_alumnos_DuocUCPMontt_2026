espada = "1"
pico = "2"
print("----Estas en la mesa de crafteo----")
print("opcion 1 es: Espada")
print("opcion 2 es: Pico")
print("presiona 3 si deseas salir de la mesa de crafteo")
while True:
    opcion = int(input("¿Que deseas craftear?: "))
    if opcion == 1:
        print("¡Espada crafteada!")
        break
    elif opcion == 2:
        print("¡Pico listo!")
        break
    elif opcion == 3: 
        print("has salido de la mesa de crafteo")
        break
    if opcion != (1,2,3):
        print("Receta desconocida. Intenta nuevamente")
    