print("###bienvenido###")
kilometro = 0
dia = 1
while dia < 8 :
    recorrido = int(input(f"cuantos kilometros corriste el dia {dia}"))
    kilometro = kilometro + recorrido
    if recorrido < 0 :
        print("dia saltado")
        kilometro = kilometro - recorrido
    dia = dia + 1
    print(f"llevas recorrido en total {kilometro} kilometros")
print("###fin de la semana###")
if kilometro > 30 :
    print("¡meta semanal cumplida!, eres un atleta.")
elif kilometro < 30 :
    print(f"sigue intentandolo llevas {kilometro} kilometros, ¡tu puedes!")  
print("fin")     