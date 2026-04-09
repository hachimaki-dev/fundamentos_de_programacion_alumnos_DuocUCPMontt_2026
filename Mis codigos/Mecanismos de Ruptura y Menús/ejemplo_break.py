
# break: El freno de emergencia
# Rompe el ciclo inmediatamente. 
# Ya no importa si la condición del while sigue siendo True, el programa salta fuera del bucle y continúa ejecutando lo que haya después.

while True:
    palabra = input("Escribe una palabra (salir para terminar): ")
    if palabra == "salir":
        break  # <--- Rompe el ciclo por completo
    print("Ingresaste:", palabra)