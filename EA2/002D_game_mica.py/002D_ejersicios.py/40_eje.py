mochila = ['mapa', 'espada']
pisoencontraste = ['madera', 'piedra', 'oro']
for ojetos in pisoencontraste:
    mochila.append(ojetos)
    if len(mochila) == 4:
        print(f"lleno{mochila}")
        break