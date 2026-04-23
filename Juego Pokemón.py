opcion= 0

print("-----Bienvenido a Pokemon Masters RPG-----")
input("Para continuar despues de que aparezca un texto, deberas presionar cualquier ENTER.")
nombre_jugador = input("Introduce tu nombre: ")
nombre_rival = input("Introduce el nombre de tu rival:")
inventario_del_jugador = ["Pokebola Normal", "Pokebola Normal", "Pokebola Normal", "Pokebola Normal", "Pokebola Normal", "Pocion De Vida Para Pokemon"]
print(f"Hola, {nombre_jugador}, bienvenido a este maravilloso mundo, donde criaturas mágicas caminan junto a nosotros los humanos")
input()
print("Te levantas temprano por la mañana, emocionado por que sera el dia en que te convertiras en un entrenador Pokemon, Tu madre te dice que vayas a hablar con el profesor Oák, para que te de instrucciones sobre como iniciar tu aventura.")

input()

print("Te diriges hacia el laboratorio del profesor Oák y al llegar el te recibe con una sonrisa y un apreton de manos.")

input()

print("A continuacion, el profesor Oák te indica que debes elegir a tu Pokemon inicial, miras la mesa con atencion, y te das cuenta de que hay 3 Pokebolas las cuales contienen 1 Pokemon cada una, el profesor Oák las lanza al suelo y tu puedes obvservar los diferentes Pokemon que salieron de alli.")

input()

while True:
  print("-----Elige tu Pokemon inicial-----")
  print("1. Charmander")
  print("2. Bulbasaur")
  print("3. Squirtle")
  
  Eleccion_De_Pokemon= input("Introduce alguna opcion:")
  
  if Eleccion_De_Pokemon == "1":
    Charmander_PS = 26
    Charmander_Ataque = 18
    Charmander_Agilidad = 45
    Charmander_Defensa = 18
    print("Perfecto, has elegido a Charmander como tu compañero de aventuras, Tu charmander tiene 26 PS, 18 Ataque, 45 Agilidad y 18 de Defensa.")
    break
  elif Eleccion_De_Pokemon == "2":
    Charmander_PS = 26
    Charmander_Daño = 18
    Charmander_Agilidad = 45
    Charmander_Defensa = 18
    print("Perfecto, has elegido a Bulbasaur como tu compañero de aventuras, Tu balbusaur tiene 20 PS, 15 de Ataque, 37 de Agilidad y 17 de Defensa.")
    break
  elif Eleccion_De_Pokemon == "3":
    print("Perfecto, has elegido a Squirtle como tu compañero de aventuras, Tu Squirtle tiene 33 PS, 22 de Ataque, 35 de Agilidad y  ")
    break
  else:
    print("Opcion no válida, porfavor, intentalo de nuevo.")
    
input()

print("El profesor Oák te mira, sonrie y te felicita debido a que al fin te has convertido en un Entrenador Pokemon.")

input()

print("El profesor Oák te pide que le vayas a comprar algo a la tienda, tu aceptas y le dices que volveras pronto.")

input()

while True:
  print("-----Que quieres hacer ahora?-----")
  print("1. Ir a comprar lo que necesita el Profesor Oák.")
  print("2. Guardar la partida y terminar el juego.")
  
  opcion1 = input("Introduce una opcion:")
  
  if opcion1 == "1":
    print("Excelente, a continuacion te diriges hacia la tienda a comprar lo que necesita el profesor Oák.")
    break
    
  elif opcion1== "2":
    print("Acabas de guardar la partida, Vuelve pronto!.")
    break
    
  else:
    print("Escoge una opcion válida.")
    
input()

print("Vas caminando por la Ruta hasta que te das cuenta de que algo se mueve entre la densa hierba.")

input()

print("Decides acercarte para ver que es lo que se mueve...")

input()

print("Wow! un Pokemon se arroja encima tuyo y no tienes otra opcion mas que lanzar a tu Pokemon al combate.")

input()

while True:
  
  print("-----Elige que ataque hacer:-----")
  print("1. Atacar")
  print("2. Abrir Mochila")
  print("3. Huir")
  
  opcion2 = input("Elige una opcion")
  
  if opcion2 == "1":
    print("Has atacado al Pokemon que salio de la hierba y le has ganado. Como recompensa conseguiste 100 EXP")
    break
    
  elif opcion2 == "2":
 
    print("Abres tu mochila para decidir si ocupar algún objeto dentro de esta")
    break
print("Tras lidiar con aquel Pokemon que apareció en la hierba, continúas con la encomienda del profesor Oák dirigiéndote hacia la tienda.")
input()

print("Ya en la tienda, compras lo que el profesor te encargó")
input()

print("Viendo las vitrinas sientes que quizás deberías aprovechar la instancia para comprar algo... O quizás solo es el consumismo surgiendo dentro de tí")

decision_tienda = input("¿Deseas ver los productos a la venta, o sólo te irás?  1. Comprar Objeto    2. Irte     ")
while True :
  if decision_tienda == "1" :
    print("Decides ver las opciones de objetos que tienen a la venta y te sorprendes por su repertorio")
    print("Con el dinero de la mensualidad que te daban tu madre y tu padre, y analizando los precios, tus 3 mejores opciones de compra son:")
    while True :
      compra_tienda = input(f" 1. 3 Pociones Curativas (Capaces de curar 20PS's a tus Pokemon)    2. Comprar 1 Revivir.Máx (Puede revivir a 1 pokemon con todos sus PS)    3. Un medallón con la cara de {Tu_Pokemon_Inicial} (Completamente cosmético).    4. Te arrepientes y solo te vas.")
      if compra_tienda == "1" :
        print("Decides comprar 3 pociones curativas, ocupando todo tu dinero, pero sientes que pueden cumplir un rol importante en tu aventura.")
        # Agregar un contador con variable de objeto_curativo para contar estos objetos en la mochila.
        break
      elif compra_tienda == "2" :
        print("Prefieres comprar un Revivir Máx, que luego de la explicación que te dió el dueño de la tienda, sientes que podría cumplir un gran propósito dada tu casi nula experiencia en combates pokémon")
        break
      elif compra_tienda == "3" :
        print(f"Te dejas llevar por tu corazón y compras este lindo medallón de {Tu_Pokemon_Inicial}, para conmemorar su primer día juntos.")
        break
      elif compra_tienda == "4" :
        print("Realmente sientes que no necesitarás nada de esto así que simplemente te vas")
        break
      else :
        print("Ingresa una opción válida porfavor.")
  if decision_tienda == "2" :
    print("Solo quieres ahorrarte tu dinero para ti mismo como la persona egoísta que eres y te largas.")
    break


