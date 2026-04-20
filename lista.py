"""
Crea una lista llamada ataques = ["Impactrueno", "Ataque Rápido", "Rayo", "Cola Férrea"].
Utiliza un ciclo for básico (por valor) para imprimir en consola "Pikachu puede usar: [nombre del ataque]".
Al salir del ciclo, usa len() para imprimir un mensaje final que diga: "Pikachu tiene un total de [X] ataques disponibles."
"""

ataques = ["Impactrueno","Ataque Rapido","Rayo", "cola ferrea" ]
total_ataques = len(ataques)
for ATAQUE in ataques:
    print(f"pikachu puede usar: {ATAQUE}")
print(f"Pikachu tiene un total de {total_ataques} ataques disponibles.")

