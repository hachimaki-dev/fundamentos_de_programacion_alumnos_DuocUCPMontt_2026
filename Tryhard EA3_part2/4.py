#Ejercicio 4 — Menú interactivo (Calculadora)
#Contexto: Una calculadora de sesión simple.
#Lo que debe hacer el programa: Crea una calculadora que funciona con un menú.
#El programa lleva un total que empieza en 0. Muestra 4 opciones: 
# 1)Pide un número y lo suma al total, 
# 2) Muestra el total actual, 
# 3) Reinicia el total a 0, 
# 4)Sale del programa.
#Si elige algo que no existe, avisa y vuelve a mostrar el menú.


total=0

print("\n===============")
print("1. Suma\n2. Motrar total\n3. Reiniciar\n4. Salir")
print("===============")

while True:
    opcion_usuario=int(input("\nPor favor ingrese una opcion. "))
    if opcion_usuario==1:
        numero_1=int(input("Ingrese un numero: "))
        total+=numero_1
    elif opcion_usuario==2:
        print(total)
    elif opcion_usuario==3:
        total=0
    elif opcion_usuario==4:
        print("Chao\n")
        break
    else:
        print("Por favor ingrese una de las 4 opciones")