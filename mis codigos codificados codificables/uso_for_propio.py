# Rentaste un auto con cierto kilometraje maximo antes de que se te solicite devolverlo, un método algo extraño de renta, pero estabas algo urgído así que solo aceptaste, por cada 10km, te llegara una notificacion a tu telefono que te avisara cuanto llevas recorrido.
kmtraje_max = 500
for (kmtraje_recorrido) in range(0, 500, 10):
    print(f"Llevas {kmtraje_recorrido}, te quedan ": + kmtraje_recorrido - kmtraje_max " antes de llegar al máximo")