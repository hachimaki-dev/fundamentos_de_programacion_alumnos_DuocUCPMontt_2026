alcancia = 0
ahorro_mensual = 80000
valor_consola = 450000

contador_numero_mes = 0

while alcancia < valor_consola:
    alcancia += ahorro_mensual
    contador_numero_mes += 1
    print(f"Valor consola: ${valor_consola}")
    print(f"Haz ahorrado ${alcancia}")
    print(f"Voy en el mes {contador_numero_mes}")

print(f"Logre ahorrar ${alcancia}")