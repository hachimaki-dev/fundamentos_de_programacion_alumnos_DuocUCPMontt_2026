canciones_favoritas = ["Fly Me to the Star - Starlight Kukugumi",
                       "Guilty Eyes Fever - Guilty Kiss", 
                       "Torikoriko PLEASE!! - AZALEA",
                       "Yozora wa Nandemo Shitteru no - CYaRon!"
]
print(canciones_favoritas) # Imprime la lista
print(canciones_favoritas[2]) # Imprime el elemento con índice 2 (el tercero)
print(len(canciones_favoritas)) # Imprime la longitud de la lista (cantidad de elementos)
print(canciones_favoritas[-1]) # Imprime el último elemento de la lista

print("\n")

canciones_favoritas.append("Georgette Me, Georgette You - Ave Mujica") # Añade elemento al final de la lista
print(canciones_favoritas[-1])

canciones_favoritas.pop() # Elimina el último elemento de la lista
print(canciones_favoritas[-1])

canciones_favoritas.insert(1, "Georgette Me, Georgette You - Ave Mujica") # Inserta elemento en la posición 1, moviendo los otros elementos hacia adelante
print(canciones_favoritas[1])

print("\n")

contador = 0
for cancion in canciones_favoritas:
    print(f"El nombre de la canción {contador} es: {cancion}")
    contador += 1
