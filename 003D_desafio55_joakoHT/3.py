pichanga = 15000
schoops = 3500
c_pichanga = 2
c_schoops = 5
personas = 5

comida = (pichanga * c_pichanga) + (schoops * c_schoops) 

propina = comida * 0.10
monto_final = comida + propina
pago_por_personas = monto_final / personas

print(pago_por_personas)