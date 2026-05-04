jugadores = [
    {"nombre": "Ash", "pts": 150},
    {"nombre": "Gary", "pts": 200}
]
if jugadores[0]["pts"] > jugadores[1]["pts"]:
    print(f"{jugadores[0]["nombre"]}")
else:
    print(f"{jugadores[1]["nombre"]}")