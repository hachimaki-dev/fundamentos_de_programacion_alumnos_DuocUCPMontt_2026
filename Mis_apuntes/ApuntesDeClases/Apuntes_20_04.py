#EN VEZ DE COLOCAR MUCHOS PRINTS, ES MEJOR USAR EL FOR IN RANGE
#LISTAS = ARREGLOS / ARRAYS / ARRAY / ARRAYLIST / LIST      [ ] <--- Corchetes para las listas
#cosas_alumno = ["Amarito", 22, 1.73, True, "Marron", "Empolvados"]
#
#print(cosas_alumno)     #IMPRIME TODA LA LISTA.
#print(cosas_alumno[4])  #IMPRIME EL ELEMENTO EN LA POSICIÓN 5.

##nombre_alumnos = ["Kevin", "Blanca", "Amaro", "Vargas"]
##edad_alumnos = [22, 29, 22, 20]                         #LISTAS DE NOMBRE, EDAD, ESTATURA.
##estatura_alumnos = [1.67, 1.73, 1.70, 1.92]
##print(nombre_alumnos[1], estatura_alumnos[1], edad_alumnos[1])  #IMPRIMIRA SEGÚN EL ORDEN.
#MEJORABLE

biblioteca_steam = ["Counter-Strike", "WoW", "L4D", "StarCraft", "MedalOfHonor", "DarkSouls", "Pokemon: Rojo Fuego", "RE4", "Terraria"]
juego = input("¿Que juego compraste?")
biblioteca_steam.append(juego)  #AÑADE UN ELEMENTO AL FINAL DE LA LISTA.
juego = input("¿Que juego compraste?")
biblioteca_steam.append(juego)
juego = input("¿Que juego compraste?")
biblioteca_steam.append(juego)
print(biblioteca_steam)

biblioteca_steam.pop()
biblioteca_steam.pop()
biblioteca_steam.pop()      #REMUEVE EL ULTIMO ELEMENTO DE LA LISTA.
biblioteca_steam.pop(1)     #REMUEVE EL ELEMENTO SEGÚN LA POSICIÓN MARCADA.

contador = 0
for elemento in biblioteca_steam:
    print(f"Juego N°{contador + 1} {elemento}")
    contador+=1