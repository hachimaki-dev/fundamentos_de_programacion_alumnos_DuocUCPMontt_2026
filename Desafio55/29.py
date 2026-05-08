kcal=0
minutos=0
while kcal<300:
    minutos+=1
    if minutos<=10:
        kcal+=20
    else:
        kcal+=10
print(minutos)