ventas = [
    {'vendedor': 'Ana',    'monto': 15000},
    {'vendedor': 'Pedro',  'monto': 32000},
    {'vendedor': 'Ana',    'monto': 21000},
    {'vendedor': 'Pedro',  'monto': 8000},
    {'vendedor': 'Carlos', 'monto': 45000},
]

resumen = {}

for vendedor in ventas:
    if vendedor.get("vendedor") not in resumen.keys():
        resumen.update({vendedor.get("vendedor"): vendedor.get("monto")})
    else:
        resumen.update({vendedor.get("vendedor"): resumen[vendedor.get("vendedor")] + vendedor.get("monto")})

nombres_vendedores = list(resumen.keys())
montos_vendedores = list(resumen.values())

indice_ganador = 0
nombre_ganador = nombres_vendedores[0]

for i in range(len(montos_vendedores)):
    if montos_vendedores[i] > montos_vendedores[indice_ganador]:
        indice_ganador = i

nombre_ganador = nombres_vendedores[indice_ganador]

for nombre, monto in resumen.items():
    print(f"{nombre}: {monto}")

print(f"Ganador: {nombre_ganador}")