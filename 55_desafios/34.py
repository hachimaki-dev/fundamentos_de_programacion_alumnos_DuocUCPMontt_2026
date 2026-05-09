#Encuentra tu mejor y peor nota del semestre rápidamente.

notas_finales = [3.5, 6.2, 5.0, 2.1, 7.0]

#Reglas de Negocio: Necesitas encontrar la nota más alta y la más baja para ver si aplicas a una beca o si necesitas tutoría.

#Restricciones: No hagas ciclos manuales complicados. Python tiene dos herramientas que hacen esto por ti: `max()` y `min()`. Úsalas e imprime ambas notas separadas por un guion.

print(max(notas_finales), "-", min(notas_finales))