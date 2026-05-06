#Encuentra tu mejor y peor nota del semestre rápidamente.
#Datos Iniciales: Tus notas finales fueron `[3.5, 6.2, 5.0, 2.1, 7.0]`.
#Reglas de Negocio: Necesitas encontrar la nota más alta y la más baja para ver si aplicas a una beca o si necesitas tutoría.
#Restricciones: No hagas ciclos manuales complicados. Python tiene dos herramientas que hacen esto por ti: `max()` y `min()`. 
#Úsalas e imprime ambas notas separadas por un guion. 7.0 - 2.1
notas_finales = [3.5, 6.2, 5.0, 2.1, 7.0]
mejor_nota = max(notas_finales)
peor_nota = min(notas_finales)
print(f"{mejor_nota} - {peor_nota}")
