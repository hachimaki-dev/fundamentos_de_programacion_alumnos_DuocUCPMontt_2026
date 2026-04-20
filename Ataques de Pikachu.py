#Instrucciones:

#Crea una lista llamada ataques = ["Impactrueno", "Ataque Rápido", "Rayo", "Cola Férrea"].
#Utiliza un ciclo for básico (por valor) para imprimir en consola "Pikachu puede usar: [nombre del ataque]".
#Al salir del ciclo, usa len() para imprimir un mensaje final que diga: "Pikachu tiene un total de [X] ataques disponibles."


ataques = ["Impactrueno", "Ataque Rápido", "Rayo", "Cola Férrea"]
for i in ataques:
    print(f"Pikachu puede usar: {i}")
print(f"Pikachu tiene un total de {len(ataques)} ataques disponibles.")