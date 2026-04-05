#contador de los días
dias = 1 

#acumulador de kilometros 

#ciclo while que se ejecuta 7 veces
while dias <= 7:
    km = float(input("¿cuantos km corriste en el día? {dias}" + str(dias) + ": "))

    #si el número de km es negativo (lesión)
    if km < 0: 
        print("Día saltado")
else:
    
    total_km += km  # type: ignore
    #avanzar al dia siguente
    dias += 1  
   #resultado final 
print("\nTotal de kilómentros: {total_km}")

if total_km >= 20:
    print("meta semanal cumplida!")
else:
 print(f"sigue intentando!, llevas {total_km} km")       
