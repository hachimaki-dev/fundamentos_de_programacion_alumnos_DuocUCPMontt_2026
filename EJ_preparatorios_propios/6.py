while True:
    patente_de_auto = input("Ingrese su patente de auto :  ").upper()
    if len(patente_de_auto) < 6 or " " in patente_de_auto:
        print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")
        continue
    else:
        print(f"Patente del Auto :  {patente_de_auto}")
        break