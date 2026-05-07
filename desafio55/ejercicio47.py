

jefe = {"hp": 100, "estado": "vivo"}
print("Le pegaste un golpe critico de 150 de daño al jefe")
jefe["hp"] = jefe["hp"] - 150
if jefe["hp"] < 0:
    print("Has asesinado al jefe")
    jefe["hp"] = 0
    jefe["estado"] = "muerto"

print(jefe)