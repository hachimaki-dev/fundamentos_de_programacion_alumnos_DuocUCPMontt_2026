#Define la variable palabra con el valor 'manzana'. Crea una variable contador_a con valor 0. 
#Recorre la palabra con un ciclo for y, cada vez que encuentres la letra 'a', suma 1 al contador. 
#Al final, imprime contador_a.
palabra = "Manzana"
contador_a = 0
for palabras in palabra:
    if palabras == "a":
        contador_a += 1
print(contador_a)