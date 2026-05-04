# Ejercicio 3: Estado de aprobación
# Define una variable nota con el valor 3.5. Luego, crea una variable estado que almacene lo siguiente:

# 'Aprobado' si nota es mayor o igual a 4.0
# 'Reprobado' en caso contrario
# Finalmente, imprime estado.

nota = 3.5
estado = ""

if nota >= 4.0:
    estado = "Aprobado"
else:
    estado = "Reprobado"

print(estado)