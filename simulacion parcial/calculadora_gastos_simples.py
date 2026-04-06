#Calculadora de gastos simples
gastos_fotocopias = 0
gastos_colacion = 0 
gasto_semanal = 0
print("######## Hola, esta es tu calculadora de gastos semanales ########")

gastos_fotocopias = int(input("¿Cuánto dinero gastas al dia en promedio haciendo fotocopias?"))

print(f"Tu gasto diario ingresado fue de {gastos_fotocopias} por lo que el gasto semanal en este es de", + gastos_fotocopias * 5)

gastos_fotocopias = gastos_fotocopias * 5

gastos_colacion = int(input("Y ahora ¿Cuánto dinero gastas para tu colación diariamente?"))

print(f"Tu gasto diario ingresado para la colación fue de {gastos_colacion}, por lo que el gasto semanal en este es de", + gastos_colacion * 5)

gastos_colacion = gastos_colacion * 5
gasto_semanal = gastos_colacion + gastos_fotocopias

print(f"Por lo que tu gasto semanal total sería ${gasto_semanal} pesos")

if gasto_semanal > 20000:
    print(f"Tu gasto semanal de {gasto_semanal} supera el promedio ¡Tienes un presupuesto alto!")
else: 
    print("Tienes un gasto semanal moderado, estás haciendo un gran trabajo")
