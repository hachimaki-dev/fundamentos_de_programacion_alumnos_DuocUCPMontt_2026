cola = [
    {'nombre': 'Laura',   'tramite': 'depósito',    'minutos': 5},
    {'nombre': 'Roberto', 'tramite': 'crédito',     'minutos': 20},
    {'nombre': 'Sofía',   'tramite': 'depósito',    'minutos': 5},
    {'nombre': 'Marcelo', 'tramite': 'hipoteca',    'minutos':  35},
    {'nombre': 'Ignacia', 'tramite': 'depósito',    'minutos': 5},
]

minutos_pasados = 0
lim_tiempo = 45

atendidos = []
sin_atender = []

for cliente in cola:
    if minutos_pasados + cliente.get("minutos") > lim_tiempo:
        sin_atender.append(cliente.get("nombre"))
        minutos_pasados += cliente.get("minutos")
    else:
        atendidos.append(cliente.get("nombre"))
        minutos_pasados += cliente.get("minutos")

print(f"Atendidos: {atendidos}")
print(f"Sin atender: {sin_atender}")