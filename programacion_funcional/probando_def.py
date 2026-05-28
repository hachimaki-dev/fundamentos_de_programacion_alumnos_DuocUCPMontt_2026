def estadisticas(notas):
    # Retorna tres valores separados por coma (Python los empaqueta en una tupla)
    return max(notas), min(notas), sum(notas)/len(notas)

# Desempaquetado mágico en 3 variables:
mayor, menor, prom = estadisticas([5.0, 7.0, 6.0])
print(estadisticas([5.0, 7.0, 6.0]))