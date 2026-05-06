minutos=0
meta=300 #en kcal

while meta > 0:
    minutos+=1
    if minutos < 11:
        meta-=20
    else:
        meta-=10
    

print (minutos)            