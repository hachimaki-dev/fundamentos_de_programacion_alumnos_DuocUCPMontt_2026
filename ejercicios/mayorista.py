print("bienvenido")
chocolate = 1000
descuento1 = 10
descuento2 = 20
total = 0
print("tenemos una barra de chocolate a $1,000clp")
print("si llevas entre 5 y 10 productos, tienes un 10% de descunto, si llevas mas de 10 20% de descuento y si llevas menos de 5 no hay descunto")
orden = int(input("cuantas barras de chocolate vas a llevar"))
if orden > 10 :
    print("al llevar mas de 10 obtienes un 20% de descunto")
    total = total + orden*chocolate 
    descuento = total/100*descuento2
    total = total - descuento
    print(f"el valor total es de {total}")
elif orden > 4 and orden < 11 :
    print("al llevar esa cantidad de barras de chocolate obtienes un descuento de 10%")
    total = total + orden*chocolate
    descuento = total/100*descuento1
    total = total - descuento
    print(f"el total de tu compra seria {total}")
elif orden < 5 :
    print("al llevar esa cantidad de barras de chocolate no obtienes descuento")
    total = total + orden*chocolate
    print(f"el total de tu compra seria {total}")
