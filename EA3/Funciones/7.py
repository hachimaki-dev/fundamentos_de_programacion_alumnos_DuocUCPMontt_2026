def calcular_propina(total: int | float, percentage: int = 10) -> int | float:
    return total * (percentage / 100)

print(calcular_propina(50000))
print(calcular_propina(50000, 25))