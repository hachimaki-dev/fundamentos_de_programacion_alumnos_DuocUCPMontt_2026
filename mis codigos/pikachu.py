ataques = ["Impactrueno", "Ataque Rápido", "Rayo", "Cola Férrea"]
contador =0
for i in range(len(ataques)):
    print(f" El ataque {contador + 1} {ataques[i]}")
    contador += 1
print (f"El Pikachu tiene {contador} ataques disponibles")
#print (f"El Pikachu tiene {len(ataques)} ataques disponibles")