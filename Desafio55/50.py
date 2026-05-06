platos = {'Papas': 5000, 'Pizza': 10000}
total = platos["Papas"] + platos['Pizza']
propina = (total * 10) / 100 
total += propina
print(f"Total final: {total}")


