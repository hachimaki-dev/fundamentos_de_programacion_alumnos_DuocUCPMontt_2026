"""
🟢 Reto Fácil: Ataques de Pikachu
Ash olvidó los movimientos de su Pikachu. Revisa la base de datos
(tu lista) e imprime sus ataques.

Instrucciones:

Crea una lista llamada ataques = ["Impactrueno", "Ataque Rápido",
"Rayo", "Cola Férrea"].

Utiliza un ciclo for básico (por valor) para imprimir en
consola "Pikachu puede usar: [nombre del ataque]".

Al salir del ciclo, usa len() para imprimir un mensaje final
que diga: "Pikachu tiene un total de [X] ataques disponibles."
"""


ataques = ["Impactrueno", "Ataque Rápido", "Rayo", "Cola Férrea"]

total_ataques = len(ataques)

for atake in ataques:
    print(f"Pikachu puede usar: {atake}")

print(f"Pikachu tiene un total de {total_ataques} ataques disponibles.")
