valor_medicamento = 60000
valor_despacho = 8000
tramo_comprador = "0"
edad_comprador = 0

def precio_med_descontado(medicamento, descuento):
    medicamento = valor_medicamento
    descuento = descuento_usuario
    return medicamento - medicamento * descuento

print("Le doy la bienvenida a un programa para calcular el valor de sus medicamentos y su despacho, según su zona y edad")

while tramo_comprador == "0" and edad_comprador == 0 :
    edad_comprador = int(input("Para continuar al cálculo de sus medicamentos necesito que ingrese su edad: "))
    tramo_comprador = input("Ahora según el mapa previamente enseñado, necesito que indique a que tramo de el recorrido de despacho, pertenece su domicilio: A, B, C o D : ")
if edad_comprador <= 30 :
    descuento_usuario = 0.18
