inventario = ["mapa", "espada"]
cosas_del_suelo = ['madera', 'piedra', 'oro']




for i in range(len(cosas_del_suelo)):
    inventario.append(cosas_del_suelo[i])
    if len(inventario) == 4:
        print("Lleno")
        print(inventario)
         
        