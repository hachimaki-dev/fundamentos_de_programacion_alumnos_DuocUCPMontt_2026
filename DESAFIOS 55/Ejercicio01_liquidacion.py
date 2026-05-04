sueldobase = 500000
bonocolacion = 50000
bonomovilizacion = 30000

descuentosalud = sueldobase*0.07
descuentoafp = sueldobase*0.1

sueldoliquido= sueldobase + bonocolacion + bonomovilizacion - descuentoafp - descuentosalud

print (sueldoliquido)
