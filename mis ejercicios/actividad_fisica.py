dia = 1
km = 0 
km_hoy = 0

while dia <= 7:
    km_hoy = int(input(f"dia {dia} - ¿cuantos km corriste?: "))
    
    if km_hoy < 0:
        print("Dia saltado")
    else:
        km = km + km_hoy
        
    dia = dia + 1
        
if km >= 30:
    print("¡Meta cumplida! eres un atleta")

else:
    print(f"sigue intentando, llevas {km} km. ¡TU PUEDES!")
    
    #ayuda d ia tambien pero igual hice solo
            
    