total_a_pagar = 0
cantidad_de_productos = 0
precio = -1 #Para poner que cuando pulse 0 salga es decir que precio sea != 0 y -1 lo es

while precio != 0:
    precio = int(input("Ingrese el precio del producto (0 para finalizar): "))
    print("......Producto ingresado.....")
    if precio != 0:
        total_a_pagar += precio #Se le suma el precio del producto al total 
        cantidad_de_productos += 1 #Se le va sumando 1 producto cada ciclo

if cantidad_de_productos >= 3:
    total_a_pagar = total_a_pagar * 0.9 #APLICO EL 10% 10/100 = 0.9 

print(f"Total a pagar: ${total_a_pagar}")
print(f"Cantidad de productos: {cantidad_de_productos}")

    


    
    
    


