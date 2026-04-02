'''
1. El programa funcionará con un ciclo while indefinido (preguntando "Ingrese temperatura actual").
2. Si la temperatura ingresada es 0, el programa termina la lectura de datos.
3. El límite de peligro es 35°C. Usa un contador especial de "alertas consecutivas" inicializado en 0.
4. Si ingresas una temp >= 35, suma 1 al contador de alertas consecutivas.
5. Si ingresas una temp < 35, el contador de alertas ESTRICTAMENTE vuelve a 0 (porque ya no es consecutiva).
6. Si en cualquier momento el contador llega a 3, imprime un texto inmenso
"¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!" y finaliza el ciclo usando break.
'''

contador_alertas_consecutivas = 0

while True :
    temperatura = int (input("Ingrese temperatura actual: "))

    if temperatura == 0 :
        break
    elif temperatura >= 35 :
        contador_alertas_consecutivas += 1
    else :
        contador_alertas_consecutivas = 0

    if contador_alertas_consecutivas == 3 :
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break