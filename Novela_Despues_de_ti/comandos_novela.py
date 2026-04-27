mecanicas = ["fumar", "ir al gimnasio", "beber", "levantarse", "ir a estudiar", "felicidad", "estres"]

cigarros_fumados = 0
fumar = input("Deseas fumar?\nSi/No\nIngresa tu elección: ").strip().lower()
if fumar == "si":
    print("Decidiste fumar, te sientes relajado, aunque quizás a futuro esto sea perjudicial.")
    cigarros_fumados += 1
elif fumar == "no":
    print("Decidiste no fumar, te sientes ansioso.")
else:
    print("Ingresa una opción valida.")

ejercicio = 0
fumar = input("Deseas hacer ejercicio?\nSi/No\nIngresa tu elección: ").strip().lower()
if fumar == "si":
    print("Decidiste ir a hacer algo de ejercicio, te sientes agotado.")
    cigarros_fumados += 1
elif fumar == "no":
    print("Decidiste no ejercitarte.")
else:
    print("Ingresa una opción valida.")