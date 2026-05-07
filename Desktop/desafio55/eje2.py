auto = 5000000
ahorrado = 1500000
ahorro_mensual = 150000

# reglas de negocio 

cuanto_falta = auto - ahorrado
meses_necesarios = cuanto_falta / ahorro_mensual
print(f"faltan {meses_necesarios} meses para comprar el auto")

