# Objetivo: Prevenir que se quemen las plantas en un invernadero automatizado.
# El programa funcionará con un ciclo while indefinido (preguntando "Ingrese temperatura actual").
alertas_consecutivas = 0
while True:
    
    temperatura = float(input("Ingrese temperatura actual: "))
    # Si la temperatura ingresada es 0, el programa termina la lectura de datos.
    if temperatura == 0:
        print("Programa terminado.")
        break
# El límite de peligro es 35°C. Usa un contador especial de "alertas consecutivas" inicializado en 0.
    # Si la temperatura es mayor a 35°C, el contador de alertas consecutivas aumenta en 1.
    if temperatura > 35:
        alertas_consecutivas += 1
    #Si ingresas una temp >= 35, suma 1 al contador de alertas consecutivas.
    elif temperatura <= 35:
        alertas_consecutivas = 0
        # Si en cualquier momento el contador llega a 3, imprime un texto inmenso "¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!" y finaliza el ciclo usando break.
    if alertas_consecutivas == 3:
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break