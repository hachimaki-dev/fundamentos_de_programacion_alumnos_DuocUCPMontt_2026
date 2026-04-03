actividad = 0 
dias = 0
kilometros = 0
while dias <= 6 :
    kilometros = int(input("cuantos kilometros recorriste hoy:"))
    if kilometros > 0 :
        actividad = kilometros + actividad
        dias = dias + 1
        print(f"hoy dia {dias} recorriste {actividad} kilometros")
       
         
    elif kilometros <= 0 :
        print("dia saltado")
        dias = dias + 1 
        print(f"dia {dias} de la semana")

       
       
if actividad >= 30 :
    print("¡meta semanal cumplida eres un atleta!")
else :
    print(f"sigue intentandolo llevas {actividad} kilometros, tu puedes")






     