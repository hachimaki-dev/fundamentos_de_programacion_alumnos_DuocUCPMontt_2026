# Ejercicio 3: El Guardián (If/Else)
# Tienes una variable llamada nota.
# Debes crear una nueva variable llamada estado que guarde:
# •	'Aprobado' si nota es mayor o igual a 4.0
# •	'Reprobado' si nota es menor que 4.0
# Pista: usa un if con else.

nota = int(input("¿Cual es tu nota?: "))

if nota >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")