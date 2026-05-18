Mochila = ['mapa', 'espada']
maximo_cosas_llevar = 4
Cosas_del_piso = ['oro', 'madera', 'piedra']


for i in Cosas_del_piso:
    if len(Mochila) < maximo_cosas_llevar:
        Mochila.append(i)
    elif len(Mochila) == maximo_cosas_llevar:
        print(Mochila)
        print("Mochila llena")