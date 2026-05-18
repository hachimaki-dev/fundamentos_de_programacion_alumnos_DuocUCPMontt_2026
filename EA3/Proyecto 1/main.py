def saludo(nombre : str, numero : int):
    print(f"Hola {nombre}")
    print (2 + numero)

# saludo(input("¿Como te shamas? "), int(input("Pone un numero: ")) )

def HelloWorld(xd):
    print(xd)

# HelloWorld("print")

protagonista = {
    "name" : "Hernan el troll",
    "hp" : 100,
    "ataque" : 6,
    "magia" : 100,
    "ataquesmagicos" : [
        {"nombreataque": "Bola de Fuego",
         "potencia" : 10},
        {"nombreataque": "Lluvia magica",
         "potencia" : 12},
        {"nombreataque": "Canto Mortal",
         "potencia" : 20}, 
    ]
}

monstruo = {
    "name" : "El Termo",
    "hp" : 30,
    "ataque" : 7
}

#HelloWorld(protagonista["ataquesmagicos"][1]["nombreataque"])

def pelea(datoprotagonista, datomounstro):
    print (f"{datomounstro["name"]} ataca a {datoprotagonista["name"]}" )
    datoprotagonista["hp"]=datoprotagonista["hp"]-datomounstro["ataque"]
    print(f" La vida de {datoprotagonista["name"]} es {datoprotagonista["hp"]}")

    datomounstro["hp"] = datomounstro["hp"] - datoprotagonista ["ataque"]
    print(f" La vida de {datomounstro["name"]} es {datomounstro["hp"]}")
    

while protagonista["hp"] > 0 and monstruo["hp"] > 0:
    pelea(protagonista,monstruo)    
    
if protagonista["hp"] <=0:
    HelloWorld("te moriste wey")    
elif monstruo["hp"] <=0:
    HelloWorld("Sobreviviste")    