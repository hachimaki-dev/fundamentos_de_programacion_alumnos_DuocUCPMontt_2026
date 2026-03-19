# LETS GET THIS ROOOOOLLLLINNNGGGG!!!

print("= = = Escandalo en la ciudad contra el mar = = =")
print(("Martes, 14:37, los Cabineros rodearon la escena del crimen, era bizarro, no habia alguna pista que indicara si siquiera habia un arma involucrada en el asesinato, uno de los cabos se acerca a ti y te habla"))
print(" *'Detective... Ve algo que este fuera de lugar?'* Eljia un numero del 1-3")
print("1. Revisar el refrigerador")
print("2. Revisar el armario")
print("3. Revisar el baño")
eleccion_1 = int(input("A donde podria investigar?: "))
if eleccion_1 == 1:
    print("Te mueves con proposito hacia el refrigerador, una vez lo abres encuentras varios articulos, la mayoria te contaban una historia del criminal, se alimentaba muy mal y evidentemente no estaba bien, pero no podrias deducir nada sobre sus habitos alimenticios de solo ver su refrigerador, revisas el congelador y encuentras algo que te llama bastante la atencion, varios moldes de silicona, extraes una de las piezas y la inspeccionas, es un carambano, lo pruebas con un pedazo de carne y efectivamente punzo a travez.")
    arma_del_crimen = "Carambano"
if eleccion_1 == 2:
    print("Atravezaste la habitacion rapidamente y una vez inspeccionas el armario te encuentras con varios articulos, ropa sucia y vieja, el sujeto no tomaba mucho cuidado de su bienestar, pero entre todo eso una sola caja de zapatos que se destacaba, la abres y descubres una pistola de tubo con una botella de plastico en la punta del barril, el culprito fabrico una cruda arma silenciada y una vez ya no era util la escondio, para cualquiera que no era familair con armas solo parecia chatarra.")
    arma_del_crimen = "Pistola de Tubo"
if eleccion_1 == 3:
    print("Empujas la puerta del baño, el olor te impacta, quien sea este sujeto nunca limpio este lugar, colgando del muro hay una mascara de gas desechable, el filtro usado, tus ojos se mueven al lavamanos, dos botellas, Vinagre y Cloro, el olor no solo era suciedad, el culprito utilizo estos quimicos para asesinar a la victima con gas toxico, cruel pero efectivo...")
    arma_del_crimen = "Gas Toxico"

print(f"El cabo se te acerca denuevo *'Detective, encontro algo? Hmm? el criminal utilizo un {arma_del_crimen}? Tiene sentido, pero aun no tenemos un motivo para el asesinato, sabemos que trajo a la victima a su apartamento pero no presentaba algun signo de hostilidad antes de la noche del crimen'* Le explicas al cabo lo que deduciste, el sujeto era inestable y el descuido del apartamento lo corraboraba *'Porsupuesto, hemos terminado la identificacion y podemos decir con certeza que la victima era el jefe del culprito, pero seguimos sin un motivo'*")
print("Decides continuar tu inspeccion, un motivo... Elije un numero del 1-3")
print("1. Revisar el computador")
print("2. Revisar el la comoda")
print("3. Interrogar al terrateniente")
eleccion_2 = int(input("Que podriamos encontrar?: "))
if eleccion_2 == 1:
    print("Inicias el computador, el culprito no tenia muchas redes sociales, pero en los correos electronicos encuentras algo interesante, varias subscripciones a sitios en linea, foros y noticias perteneciendo a una motivacion militante, el criminal asesino a su jefe porque se convencio que era necesario, que su jefe era un parasito y que era su deber matarlo por el bein mayor.")
    motivo_del_crimen = "Motivacion Politica"
if eleccion_2 == 2:
    print("Abres la comoda y descubres vouchers, cupones, y una tarjeta de membresia a un casino, interesante, el sujeto vivia con un presupuesto basico y aun asi apostaba con lo poco que tenia en sus bolsillos, lo que no encuentras es medicina, si tu teoria de que el culprito sufria de alguna enfermedad mental talvez podrias encontrar algo que sugiera tratamiento, claro, si gastaba todo en el casino no tendria nada para su tratamiento, un ciclo sin fin.")
    motivo_del_crimen = "Motivacion Avara"
if eleccion_2 == 3:
    print("Decides interrogar al terrateniente, un hombre que tenia una aparencia dura *'Que? Estoy ocupado! Ah, el... Bah! Nunca me agrado el sujeto, le subi la renta porque siempre causaba problemas con los vecinos, si tan solo fuera normal no tendria que lavar su pizo de sangre, inutil!'* Escuchaste suficiente, si consideras que el sujeto era inestable junto a que su terrateniente lo trataba como un problema mas que uno de sus habitantes, con suerte prodria pagar su renta si a penas mantenia su apartamento en condiciones optimas.")
    motivo_del_crimen = "Motivacion Monetaria"
print(f"Te devuelves con el cabo y le reportas tu descubrimientos *'Ah, entonces el sujeto tenia una {motivo_del_crimen}, empieza a tener sentido, el sujeto claramente no tenia ayuda, sino hubieramos encontrado medicina en algun sector del apartamento, pero lo ultimo que tenemos que deducir es porque asesino a su jefe? Que tenia el que ver con esto?'* Claro, era ora de comparar nuestra evidencia para ver si podemos encontrar un motivo claro para aclarar el crimen")
if arma_del_crimen == "Carambo" and motivo_del_crimen == "Motivacion Avara":
    print("Ahora tiene sentido, el criminal invito a su jefe bajo algun pretexto de trabajo, pero el criminal lo asesino con el Carambo para que la evidencia del crimen desapareciera, la billetera ya no estaba, el culprito estaba tan obsecionado con apostar que fue por el objectivo mas grande y escapo sin dejar un rastro, pero ahora con la imagen completa podemos buscarlo, casinos, su habitat, lo traeremos a la justicia **FIN GRACIAS POR JUGAR!**")
if arma_del_crimen == "Pistola de Tubo" and motivo_del_crimen == "Motivacion Politica":
    print("Ahora todo tiene sentido, el culprito fabrico un arma y asesino a su jefe porque se volvio loco con su vision politica, invito a su jefe y lo mato como mensaje a los demas, de que el vendria por el proximo, que no descansaria hasta que aquellos que el veia como parasitos estaran muertos a sus pies, no teniamos un ratros pero con los vinculos a grupos politicos podremos encontrarlo, no limpio sus rastros bien, lo encontraremos **FIN GRACIAS POR JUGAR!**")
if arma_del_crimen == "Gas Toxico" and motivo_del_crimen == "Motivacion Monetaria":
    print("Ahora tiene sentido, el culprito utilizo materiales inconspicuos para no llamar la atencion, trajo a su jefe a su apartamento y utilizo la mascara de gas para sobrevivir mientras la victima sufria, podemos asumir de que si queria mantenerse en la misma habitacion que la victima entonces queria interactuar, posiblemente estaba trantando de negociar, si el sujeto estaba tan escaso en capital entonces queria demandarle a su jefe que le diera un aumento, dinero, algo para escapar de este agujero en el que se encontraba, la billetera estaba vacia de dinero por lo tanto podemos asumir de que la victima fallecio y no le entrego nada al culprito, pero tenemos evidencia de sus huellas y sus motivos, lo encontraremos **FIN GRACIAS POR JUGAR!**")
else:
    print("La evidencia es insuficiente, no se acopla... De alguna forma logro el crimen perfecto, pero no podemos rendirnos, lo encontraremos, y lo traere a la justicia... **FIN GRACIAS POR JUGAR!**")
