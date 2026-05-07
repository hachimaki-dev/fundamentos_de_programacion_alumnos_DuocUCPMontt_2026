Minutos = 0
Calorias = 0
Metas_de_Calorias = 300

while Calorias < 300 :

    Minutos += 1

    if Minutos <= 10:
        Calorias += 20

    else:
        Calorias += 10

print(f"Tardaste {Minutos} minutos")