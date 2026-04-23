persona = {
    "nombre": "Carla",
    "edad": 22,
    "notas": [6.0, 5.8, 7.0]
}

print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Notas:", persona["notas"])

suma = 0
for nota in persona["notas"]:
    suma += nota

promedio = suma / len(persona["notas"])
print("Promedio:", promedio)