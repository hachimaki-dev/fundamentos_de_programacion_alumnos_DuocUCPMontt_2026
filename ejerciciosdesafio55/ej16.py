cliente = "postpago"
su_plan = 15 #gb
uso = 18 #gb
if cliente == "postpago":
    if uso > su_plan:
        extra = uso - su_plan
        cobro = extra * 1000
else:
    print("sin saldo")
    cobro = 0
print(cobro)