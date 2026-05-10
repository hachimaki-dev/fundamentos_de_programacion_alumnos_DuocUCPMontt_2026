peso = 25
cobertura = 'A'
primamensual=22000
chip=9000


if peso >= 20:
    if cobertura == 'A' or cobertura == 'B':
        primamensual -= primamensual*0.16
    elif cobertura == 'C' or cobertura == 'D':
        primamensual -= primamensual*0.1
elif 8 <= peso < 20:
    if cobertura == 'A' or cobertura == 'B':
        primamensual -= primamensual*0.1
    elif cobertura == 'C' or cobertura == 'D':
        primamensual -= primamensual*0.06
else:
    primamensual=primamensual 

#chip

if cobertura == 'A' or cobertura == 'B':
    chip -= chip*0.12
    if peso >= 15:
        chip -= chip*0.06
                  
print(f'El valor de su plan mensual es ${int(primamensual)}') 
print(f'Su cargo de chip es ${int(chip)}')
                