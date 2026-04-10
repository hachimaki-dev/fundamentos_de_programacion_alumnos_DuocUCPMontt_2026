
print("--- Bienvenido Steve a tu mesa de crafteo---\n")
print("1. Espada de Diamante ⚔️")
print("2. Pico ⛏️")
print("3. Salir de la mesa de crafteo\n")

while True:    
    herramienta = input("¿Qué deseas craftear? ⚒️\n(Presiona 3 para salir)\n")
    if herramienta == "3":
        print("Saliste de la mesa de crafteo")
        break
    elif herramienta == "1":
        print("Espada crafteada ⚔️")
    elif herramienta == "2":
        print("¡Pico listo! ⛏️")
    else:
        print("Receta desconocida. Intenta nuevamente")
        continue
