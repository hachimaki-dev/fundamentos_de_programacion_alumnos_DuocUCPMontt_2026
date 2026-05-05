#Pasó un 'Camion' a 95 km/h.
#Los autos no pueden pasar de 120 km/h (si se pasan, es 'Multa Gravísima')
#Los camiones son más pesados y no pueden pasar de 80 km/h (si se pasan, es 'Multa Grave Camión').
#Si van bajo sus límites, no hay multa

tipo_vehiculo = input("Ingresa tu tipo de vehiculo (auto/camion):")
velocidad = int(input(" ingresa tu velocidad en km/h: "))

if tipo_vehiculo == "auto" and velocidad > 120:
    print("MULTA GRAVISIMA")
elif tipo_vehiculo == "camion" and velocidad > 80:
    print("MULTA GRAVISIMA CAMION")
else:
    print("sin multa")