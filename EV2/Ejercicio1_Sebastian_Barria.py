#Calculadora Valor Medicamentos

mensualidad_medicamentos = 60000
tramo_comprador = "0"
edad_comprador = 0
valor_despacho = 8000
print("Hola, le doy la cordial bienvenida a un programa que le permitirá calcular el precio de sus medicamentos agregando además el despacho")

while tramo_comprador == "0" and edad_comprador == 0 :
    edad_comprador = int(input("Para ello voy a necesitar que primero me ingrese su edad, siendo completamente honesto "))
    tramo_comprador = input("Ahora necesito que especifique si usted pertenece al tramo A, B, C o D previamente especificados en la aplicación ")
if tramo_comprador == "a" or tramo_comprador == "b" and edad_comprador <= 30 :
    mensualidad_medicamentos = mensualidad_medicamentos - mensualidad_medicamentos * 0.18
    valor_despacho = valor_despacho - valor_despacho / 10
    print(f"El valor de sus medicamentos sería:{mensualidad_medicamentos}")
    print(f"Y el valor de su despacho sería: {valor_despacho}")
elif tramo_comprador == "c" or tramo_comprador == "d" and edad_comprador <= 30 :
    mensualidad_medicamentos = mensualidad_medicamentos - mensualidad_medicamentos * 0.12
    print(f"El valor total de sus medicamentos sería: {mensualidad_medicamentos}.")
    print(f"Y el despacho: {valor_despacho}.")
elif 31 <= edad_comprador and edad_comprador <= 60 and tramo_comprador == "a" or tramo_comprador == "b" :
    mensualidad_medicamentos = mensualidad_medicamentos - mensualidad_medicamentos * 0.12
    valor_despacho = valor_despacho - valor_despacho * 0.10
    if edad_comprador >= 55 :
        valor_despacho = 8000 - 8000 * 0.15
    print(f"El valor de sus medicamentos sería: {mensualidad_medicamentos}.")
    print(f"Y el de su despacho: {valor_despacho}")
elif 31 <= edad_comprador and edad_comprador <= 60 and tramo_comprador == "c" or tramo_comprador == "d" :
    mensualidad_medicamentos = mensualidad_medicamentos - mensualidad_medicamentos * 0.08
    print(f"El costo de sus medicamentos terminaría siendo: {mensualidad_medicamentos}")
    print(f"Y el de su despacho: {valor_despacho}")
