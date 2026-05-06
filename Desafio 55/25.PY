censura_1="noob"
censura_2="manco"
contador=0
lista_mensajes=["hola","noob","genial","manco"]

for  mensaje in  lista_mensajes:
    
    if mensaje==censura_1 or mensaje==censura_2:
        lista_mensajes[contador] = "Cesurado"
    contador+=1

print(lista_mensajes)