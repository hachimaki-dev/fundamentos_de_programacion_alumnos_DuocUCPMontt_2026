tipo = "Postpago"
plan = 15
gigas_usados = 18

gigas_extras = gigas_usados - plan
precio_gigas_extras = 1000

if tipo == "Postpago":
    recargo_final = gigas_extras * precio_gigas_extras
else:
    print("Sin saldo")

print(recargo_final)