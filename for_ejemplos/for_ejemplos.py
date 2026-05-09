mis_notas = [6.5, 5.0, 4.0]
# El método len contaría 3 objetos. Por deducción matemática range(3)
# arrojará iteración posicional: el 0 pasivo, el 1 continuo, el 2 base.

for contador_de_posicion in range(len(mis_notas)):
    mis_notas[contador_de_posicion] = mis_notas[contador_de_posicion] + 0.1

print(mis_notas) 
"""Resalta modificativamente permanente [6.6, 5.1, 4.1] <- Éxito masivo inyectado"""
"""en servidor variables """