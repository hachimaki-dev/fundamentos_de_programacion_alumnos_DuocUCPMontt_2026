tipo_vehiculo = "Camión"
velocidad = 95

print("La cámara de seguridad ha detectado un camión a gran velocidad")
print("Por ley los vehiculos solo pueden ir a 120KM/h pero al ser un vehiculo pesado como un camión, debe de ir a 80 KM/h máximo.")

if tipo_vehiculo == "Auto" and velocidad > 120:
    print("EXCESO DE VELOCIDAD, MULTA GRAVISIMA.")
elif tipo_vehiculo == "Camión" and velocidad > 80:
    print("EXCESO DE VELOCIDAD, MULTA GRAVISIMA CAMIÓN")
else:
    print("No se aplicara ninguna multa")