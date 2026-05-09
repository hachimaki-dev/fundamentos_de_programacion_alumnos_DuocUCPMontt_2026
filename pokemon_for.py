"""Ash olvidó los movimientos de su Pikachu. Revisa la base de datos 
(tu lista) e imprime sus ataques.

Instrucciones:

Crea una lista llamada ataques = ["Impactrueno", "Ataque Rápido",
 "Rayo", "Cola Férrea"].

Utiliza un ciclo for básico (por valor) para imprimir en consola 
"Pikachu puede usar: [nombre del ataque]".

Al salir del ciclo, usa len() para imprimir un mensaje final que diga: 
"Pikachu tiene un total de [X] ataques disponibles."""

ataques = [ "impactrueno" , "ataque rapido", "rayo", "cola ferrea" ]

for ataque in ataques:
    print(f"pikachu puede usar:55 {ataque}")

print(f"pikachu aun tiene un total de {len(ataques)} ataques disponible")