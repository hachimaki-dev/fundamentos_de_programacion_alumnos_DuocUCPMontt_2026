km_acumulados = 0
dia = 0

print("~~~¡Bienvenido a tu Smartwatch! Vamos a registrar tus kilómetros semanales. La meta es de 30 km por semana. Si no puedes correr un día, ingresa -1 para saltar ese día.~~~")
while dia < 7:
    km_de_hoy =int(input("Cuantos km corriste el dia Lunes?"))
    if km_de_hoy == -1:
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")
    

    km_de_hoy =int(input("Cuantos km corriste el dia Martes?"))
    if km_de_hoy == -1:
        dia += 1
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")

    km_de_hoy =int(input("Cuantos km corriste el dia Miercoles?"))
    if km_de_hoy == -1:
        dia += 1
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")
    
    
    km_de_hoy =int(input("Cuantos km corriste el dia Jueves?"))
    if km_de_hoy == -1:
        dia += 1
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")
    
    km_de_hoy =int(input("Cuantos km corriste el dia Viernes?"))
    if km_de_hoy == -1:
        dia += 1
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")

    km_de_hoy =int(input("Cuantos km corriste el dia Sabado?"))
    if km_de_hoy == -1:
        dia += 1
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")

    km_de_hoy =int(input("Cuantos km corriste el dia Domingo?"))
    if km_de_hoy == -1:
        dia += 1
        print("Día saltado")
    else:
        km_acumulados += km_de_hoy
        dia += 1
        print(f"km acumulados: {km_acumulados}")

if km_acumulados >= 30:
    print("¡Meta semanal cumplida! Eres un atleta")
else: 
    print(f"Sigue intentando, llevas {km_acumulados} kilómetros, ¡tu puedes!")