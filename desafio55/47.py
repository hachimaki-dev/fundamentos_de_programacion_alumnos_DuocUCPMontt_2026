jefe = {"HP": 100, "Estado": "Vivo"}
ataque = 150
jefe["HP"] -= ataque
if jefe["HP"] < 0:
    jefe["HP"] = 0
    jefe["Estado"] = "Muerto"
print(jefe)