#Ejercicio 5: Suma con for
#Crea una variable resultado con valor 0. Usa un ciclo for y range() para sumar todos los números desde 0 hasta 10, incluyendo el 10.
# Al final, imprime resultado.

#Pista: range(11)

#Resultado esperado en consola:
#55

resultado=0
for i in range(0, 11):
    resultado+=i
    print(resultado)