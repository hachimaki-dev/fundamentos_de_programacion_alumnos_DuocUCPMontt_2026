cliente = "postpago"
plan = 15 
gasto = 18

if cliente == 'Postpago':
    if gasto > plan:
        recargo = (gasto - plan) * 1000
        print(recargo)
else:
    print(3000)