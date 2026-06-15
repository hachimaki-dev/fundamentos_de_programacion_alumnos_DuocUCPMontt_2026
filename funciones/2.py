def calcular_multa(dias_atraso, valor_por_dia=100):
    return dias_atraso * valor_por_dia

# 1. Prueba con un solo argumento (usa el valor por defecto: 100)
multa_caso_1 = calcular_multa(5)
print(f"Multa con 5 días de atraso (valor por defecto): ${multa_caso_1}")

# 2. Prueba con dos argumentos (reemplaza el 100 por 250)
multa_caso_2 = calcular_multa(5, 250)
print(f"Multa con 5 días de atraso (valor personalizado de $250): ${multa_caso_2}")