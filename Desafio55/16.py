tipo_c = "Postpago"
plan_c =  15
uso_de_gb = 18
extras = 3 * 1000
if tipo_c == "Postpago":
    if uso_de_gb > plan_c:
        uso_de_gb -= plan_c
        uso_de_gb = uso_de_gb * 1000
        print(uso_de_gb)