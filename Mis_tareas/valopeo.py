'''
Inicializa una variable contador en cero (ejemplo: arma = 0) y utiliza un ciclo while configurado para iterar hasta procesar las 5 armas.
Asegúrate de realizar obligatoriamente el incremento de la variable de control de iteración (arma += 1) en la primera línea dentro del bucle antes de evaluarlo. Modificar esto mal causaría un loop sin avance infinito en las etapas donde logres hacer bypass temporal por medio excepcional con su evaluadas líneas interrumpiendo bloque de evaluación en ejecución.
Verifica con condicionales el número actual del objeto: si el valor iterado es exactamente igual a 4, el programa deberá únicamente imprimir en pantalla "Arma 4: Notificación - Agotada" y utilizar la sentencia continue al final de ese pequeño if para interrumpir el flujo inferior provocando que ignore y obvie directamente procesar simulaciones de compra inferiores brincando al punto pre evaluación y logrando comenzar ciclo del siguiente armamento iterado.
En cualquier caso del código restante y ajeno a ese filtro inferior que proceda a visualizar el resto de numeración habilitada deberás simplemente ejecutar el imprimir del mensaje indicativo exitoso iterando valor: "Comprando exitosamente el arma número [X]".
'''
contador=0
while contador <10 :
    contador +=1
    if contador%2==0:
        print(f"Arma {contador} agotada")
        continue
    else:
        print(f"comprando exitosamente el arma numero {contador}")