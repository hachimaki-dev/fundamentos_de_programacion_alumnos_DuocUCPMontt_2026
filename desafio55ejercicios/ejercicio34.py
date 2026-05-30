""" Ejercicio 34: Top Notas (Portal Alumno)
Encuentra tu mejor y peor nota del semestre rápidamente.

Datos Iniciales: Tus notas finales fueron `[3.5, 6.2, 5.0, 2.1, 7.0]`.

Reglas de Negocio: Necesitas encontrar la nota más alta y la más baja para ver si aplicas a una beca o si necesitas tutoría.

Restricciones: No hagas ciclos manuales complicados. Python tiene dos herramientas que hacen esto por ti: `max()` y `min()`. 
Úsalas e imprime ambas notas separadas por un guion."""

notas = [3.5, 6.2, 5.0, 2.1, 7.0]


nota_mas_baja = min(notas)
nota_mas_alta = max(notas)
print(f"{nota_mas_alta}")
print(f"{nota_mas_baja}") 