boss = {
    'hp': 100, 
    'estado': 'vivo'
}

print("Golpe Critico! -150")
boss["hp"] -= 150

if boss["hp"] <= 0:
    boss["estado"] = "muerto"
    boss["hp"] = 0
    
print(boss)
