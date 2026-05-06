tipo_veiculo = "camion"
kilometraje = 95

if tipo_veiculo == "auto" and kilometraje >= 120:
    print("multa gravisima")

elif tipo_veiculo == "camion" and kilometraje >= 80:
    print("Multa Grave Camión")

else:
    print("no hay multa")