palabra_base = "user_"
contador = 1


for palabra in (palabra_base):
    palabra_base = palabra_base+str(contador)
    contador += 1
    print(palabra_base)
    palabra_base = "user_"