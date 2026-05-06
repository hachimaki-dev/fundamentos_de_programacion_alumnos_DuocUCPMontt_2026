sueldo= 550000
deudas_activas= 1
if sueldo > 500000 and deudas_activas == 0:
    print(f"Tu sueldo es de {sueldo} y tus deudas activas son {deudas_activas}")
    print("Credito aprobado!")
else:
    print(f"Tu sueldo es de {sueldo} y tus deudas activas son {deudas_activas}")
    print("Credito rechazado, no cumples las condiciones")
