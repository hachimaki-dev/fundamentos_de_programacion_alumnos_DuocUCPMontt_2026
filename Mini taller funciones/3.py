def Crear_multa(dias_atraso, valor_por_dia = 100):
    return dias_atraso * valor_por_dia
a = Crear_multa(5)      #SI EL PARAMETRO DE LA FUNCION TIENE UN VALOR DEFAULT (ASIGNADO DENTRO DEL PARAMETRO), ENTONCES PODEMOS COLOCAR SOLO 1 ARGUMENTO
b = Crear_multa(5, 250)  #CASO CONTRARIO: SE REASIGNA EL VALOR DEL PARAMETRO QUE TIENE UN VALOR ASIGNADO COMO DEFAULT, valor_por_dia = 100 -> 250
print(f"{a} | {b}")
