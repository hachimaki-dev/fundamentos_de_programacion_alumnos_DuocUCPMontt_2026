# Solo dejamos un anime para la prueba
series = {'AN001': ['Attack on Titan', 'accion', 'MAPPA', 'M', False, 'Japon']}
catalogo = {'AN001': [9990, 75]}

codigo = 'AN001'


def episodios_por_genero(genero_a_buscar):
    contador_de_episodios = 0

    genero_a_buscar_limpio = genero_a_buscar.strip().lower()

    for id in series:
        genero_actual = series[id][1].strip().lower()

        if genero_a_buscar_limpio == genero_actual:
            cantidad_de_episodios = catalogo[id][1]
            contador_de_episodios += cantidad_de_episodios
    print(f"La cantidad de episodios del genero {genero_a_buscar_limpio} es de: {contador_de_episodios}")

