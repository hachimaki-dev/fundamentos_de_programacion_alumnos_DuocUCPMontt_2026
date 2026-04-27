turno=1
vida=100
vida_enemigo=250
eleccion=0
derrotas=0
respuesta=0
mood="neutral"
tienda=[f"1-Abrigo largo: $100", "2-Calzas negras: $50", "3-Botas de piel de huargo: $200","4-Calcetines de lana: $10", "5-Vestido blanco: $300", "6-Aretes de plata: $400", "7-collar de rubi: $500" ]
compra=0
dinero=0
estado="Indecente"
actividades=[f"1-Cazar bestias -30 monedas + 20 monedas  por monstruo abatido (Tiempo medio)", f"2-Atender de dia a noche la taberna -60 monedas (Todo el dia)",f"3-Limpiar la herreria -20 monedas (Poco tiempo)", f"4-Alimentar a los caballos 10 monedas (Poco tiempo)",f"5-Ayudar al escriba 40 monedas (Tiempo moderado)","6-Meditar (Tiempo moderado)",f"7-Comprar",f"8-No hacer nada (Saltar dia)",f"9-Ver inventario"]
accion=0
estatus=[dinero, estado,mood]
combate=0
inventario=["Libro de magia", "Foto de tu familia"]
plazo = 14
dias=0

print("===============================================================")
print("")
print("El primer pecado: Acto II ")
print("")
print("===============================================================")
print("")
input("Pulse cualquier boton para comenzar: ")
print("")
print("")
print("Luego de caminar por dias y dias por fin llegas Demarron el reino de los demonios")
print("Antes de entrar miras tus manos, estaban temblando y aun con sangre despues de habertelas limpiado")
print("Por un momento recuerdas lo que tuviste que hacer, tus ojos se ponen llorosos, pero cierras tus manos con fuerza")
print("(tengo que seguir) Pensaste, ahora ante tus ojos se alza imponente Derramon, donde quizas encuentres al demonio mago que queria conocerte")
print("Ante ti se acerca un guardia, habia sospechado de ti por quedarte parada durante un buen tiempo ")
print("Guardia: Saludos elfa, por favor podria identificarse")
print("Dahlia: Oh claro solo deme un momento")
while True:
    print("Tienes que pensar en algo, si das tu nombre tal vez te culpen de un crimen, quizas un nombre falso ")
    respuesta = int(input("Que vas a responder "))
    if respuesta== 1:
        print("Dahlia: Me llamo Dahlia, vengo a hablar con el demonio mago")
        print("Guardia: Señorita, me han informado que usted ha cometido un crimen por estas tierras, me veo en la obligacion de llevarla ante mi superior")
        print("Dahlia: N-no es lo que cree yo-")
        print("Guardia: Tengo que llevarmela, por su bien no intente defenderse")
        print("Antes de que puedas hablar en tu defensa el guardia te habia atrapado los brazos, estas demasiado cansada para defenderte con magia...")
        break
    elif respuesta ==2:
        print("Dahlia: Mi nombre es... Amelia, si me llamo Amelia")
        print("El guardia noto duda en tu tono de voz")
        print("Guardia: Amelia eh, no conozco a ninguna elfa llamada asi, ninguna tiene ese nombre")
        print("Guardia: Tienes que venir conmigo, tengo que interrogarte")
        print("El guardia te toma de los brazos sin que puedas hacer nada, te has metido en problemas")
        break
    else:
        print("accion invalida")
print("El guardia te lleva a rastras por todo el reino, la humillacion que sientes no tiene explicacion")
print("Sientes como te raspas con el suelo")
print("Dahlia: Basta... Me estas hiriendo")
print("El guardia hizo oidos sordos, el tramo fue largo y doloroso, pero ya llegaste al cuartel donde te van a juzgar")
print("Guardia: Esperaremos aqui hasta que llegue el general")
print("Te quedas en silencio durante horas hasta que el general llego")
print("Un demonio mas alto de lo normal, con cabellos blancos, los ojos de un color carmesi")
print("Su mera precensia impuso un escalofrio en todo tu cuerpo")
print("General: Una elfa de pelos blancos, que peculiar...")
print("El general te observa detenidamente, notando que haz sido agredida por el guardia")
print("General: Kerval, que te he dicho de tratar a la gente asi, en especial a los elfos")
print("Kerval: Pe-pero general Cralvohz-")
print("Cralvohz: Silencio, ya hablare contigo cuando termine con ella, ahora vete")
print("Cralvohz: Lamento el actuar de mi subordinado, disculpeme, pero no se que puedo hacer para remediar esta situacion")
print("Dahlia: Podria llevarme con el mago demonio por favor")
print("Cralvohz: Angluxis no se encuentra presente, volvera en una semana, tendras que quedarte aqui por el momento")
print("Cralvohz: Que tal si te alojas en mi casa, mienrtas el llega, seras mi protegida, se muy bien el crimen que hiciste, pero no creo que seas culpable")
print("Dahlia: Gracias señor, por su bondad")
print("Cralvohz: No hace falta agradecerme, ahora vamos, seguramente debes estar cansada por todo lo que te ha acontecido")
print("Asientes y sigues al demonio hasta sus aposentos, al llegar encuentras un lugar limpio y ordenado, tus padres siempre te habian dicho que los demonios no eran muy ordenados")
print("Cralvohz: Puedes utilizar la habitacion de mi hermana mientras ella no esta, mañana veremos que puedes hacer mientras esperas a Angluxis")
print("Cralvohz: Bien, nos vemos mañana, a todo esto, no te he preguntado tu nombre, como te llamas?")
print("Dahlia: Me llamo Dahlia")
print("Cralvohz: Dahlia... bonito nombre, bueno, no te molesto mas nos vemos mañana")
print("A la mañana siguiente notas como Cralvohz no estaba, pero te habia dejado una nota que decia: Tienes que trabajar y conseguir algo de dinero, quizas en el centro encuentres algo de trabajo que hacer")
print("Dahlia: Muy bien, quizas algo de dinero me sirva para comprar cosas nuevas")
print("te diriges al centro de la ciudad, puedes ver como hay multiples trabajos para hacer algo de dinero")

while dias < plazo:    
    print("Que podria hacer...")
    print(estatus)
    print("=================================================================")
#actividades=[f"1-Cazar bestias -30 monedas + 20 monedas  por monstruo abatido (Tiempo medio)", f"2-Atender de dia a noche la taberna -60 monedas (Todo el dia)",f"3-Limpiar la herreria -20 monedas (Poco tiempo)", f"4-Alimentar a los caballos 10 monedas (Poco tiempo)",f"5-Ayudar al escriba 40 monedas (Tiempo moderado)","6-Meditar (Tiempo moderado)",f"7-Comprar",f"8-Ver inventario"]
    for actividad in actividades:
        print(actividad)
    print("=================================================================")
    accion =int(input("Selecciona una actividad "))
    if accion ==1:
        print("Fuiste al gremio para hacer un encargo de cazar bestias en las afueras de la ciudad")
        print("En el bosque te topas con un monstruo, preparate para luchar")
        while True:
            while vida > 0 and vida_enemigo > 0:
                print("======================================")
                print(f"==tu vida {vida}==")
                print(f"==vida del monstruo {vida_enemigo}==")
                print("===Combate===")
                print("1-Usar magia de fuego")
                print("2-Usar magia de hielo")
                print("3-Usar magia de electricidad")
                print("4-Usar magia de tierra")
                print("5-Usar magia de viento")
                print("6-Curarte")
                print("======================================")
                combate =int(input("Que deberia hacer: "))
                if combate == 1:
                    print("usaste magia de fuego")
                    vida_enemigo -= 45
                    vida -= 15
                elif combate==2:
                    print("Usaste magiad e hielo")
                    vida_enemigo -= 50
                    vida -= 10
                elif combate == 3:
                    print("Usaste magia electrica")
                    if turno %2==0:
                        print("El monstruo se ha paralizado y no ataco")
                        vida_enemigo -= 30
                    else:
                        vida_enemigo -=25
                        vida -= 25
                elif combate == 4:
                    print("Usaste magia de tierra")
                    if turno % 3==0:
                        print("el monstruo se desestabilizo y no ataca")
                        vida_enemigo-=10
                    else:
                        vida_enemigo -=5
                        vida -=10
                elif combate==5:
                    print("Usaste magia de viento")
                    vida-=20
                    vida_enemigo-=40
                elif combate == 6:
                    if vida < 100:
                        print("Te curaste algo de vida")
                        vida += 40
                    else:
                        print("Tu vida esta al maximo")
            if vida < vida_enemigo:
                print("Saliste corriendo por no poder contra la bestia")
                estatus[2] = "Alterada"
                vida = 100
                break
            else:
                derrotas +=1
                print(f"Has derrotado a un monstruo. Monstruos derrotados:{derrotas}")
                pregunta = input("Quieres seguir buscando monstruos? S o N ").upper()
                if pregunta== "S":
                    print("Sigues explorando hasta que te topas con un monstruo")
                    vida_enemigo = 250
                else: 
                    print(f"Te vas del bosque, tu trabajo en las afueras ha terminado. Monstruos derrotados: {derrotas}")
                    estatus[0] += 30 + (20*derrotas)
                    dias +=1
                    break
    elif accion == 2:
        print("Fuiste a la taverna a atender a los demonios borrachines")
        print("El trabajo te llevo todo el dia pero valio la pena")
        estatus[0] += 60
        dias +=1
        print("Queda un dia menos para ver al demonio mago")
    elif accion ==3:
        print("Vas a la herreria para limpiar mientras el herrero trabaja")
        estatus[0] += 20
        print("Tardaste poco podrias hacer mas actividades")
        dia = input("quieres seguir haciendo actividades S o N ").upper()
        if dia == "S":
            print("Prosigues con las actividades")
        else:
            print("Te vas a casa de Cralvohz a descansar...")
            dias +=1
            print("Queda un dia menos para ver al demonio mago")

    elif accion ==4:
        print("Vas al establo a lavarle las pezuñas a los caballos")
        estatus[0] += 10
        print("Tardaste poco podrias hacer mas actividades")
        dia = input("quieres seguir haciendo actividades S o N ").upper()
        if dia == "S":
            print("Prosigues con las actividades")
        else:
            print("Te vas a casa de Cralvohz a descansar...")
            dias +=1
            print("Queda un dia menos para ver al demonio mago")
    elif accion ==5:
        print("Vas donde el escriba para ayudarlo con sus escrituras")
        estatus[0] += 40
        print("Aun puedes hacer algo en el resto del dia")
        dia = input("quieres seguir haciendo actividades S o N ").upper()
        if dia == "S":
            print("Prosigues con las actividades")
        else:
            print("Te vas a casa de Cralvohz a descansar...")
            dias +=1
            print("Queda un dia menos para ver al demonio mago")
    elif accion == 6:
        print("Vas a un lugar tranquilo a meditar un rato")
        vida +=100
        estatus[2]="tranquila"
    elif accion ==7:
        print("Te diriges a la tienda a comprar ropa, es hora de un cambio")
        #tienda=[f"1-Abrigo largo: $100", "2-Calzas negras: $50", "3-Botas de piel de huargo: $200","4-Calcetines de lana: $10", "5-Vestido blanco: $300", "6-Aretes de plata: $400", "7-collar de rubi: $500" ]
        while True:
            print("Que puedo comprar ")
            for objeto in tienda:
                print(objeto)
            compra=int(input("Elije que comprar "))
            if compra ==1:
                if estatus[0] < 100:
                    print("no tienes dinero")
                else:
                    print("Compraste un abrigo")
                    estatus[0]-=100
                    estatus[1]= "presentable"
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
            if compra ==2:
                if estatus[0] < 50:
                    print("no tienes dinero")
                else:
                    print("Compraste unas calzas negras")
                    estatus[0]-=50
                    estatus[1]="casi presentable"
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
            if compra ==3:
                if estatus[0] < 200:
                    print("no tienes dinero")
                else:
                    print("Compraste unas botas de piel de huargo")
                    estatus[0]-=200
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
            if compra ==4:
                if estatus[0] < 10:
                    print("no tienes dinero")
                else:
                    print("Compraste unos calcetines de lana")
                    estatus[0]-=10
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
            if compra ==5:
                if estatus[0] < 300:
                    print("no tienes dinero")
                else:
                    print("Compraste un vestido blanco")
                    estatus[0]-=300
                    estatus[1] = "bonita"
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
            if compra ==6:
                if estatus[0] < 400:
                    print("no tienes dinero")
                else:
                    print("Compraste unos aretes de plata")
                    estatus[0]-= 400
                    estatus[1]="casi decente"
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
            if compra ==7:
                if estatus[0] < 500:
                    print("no tienes dinero")
                else:
                    print("Compraste un collar de ruby")
                    estatus[0]-=500
                    estatus[1]="decente"
                    pregunta=input("Quieres seguir comprando? S o N ").upper()
                    if pregunta == "S":
                        print("Sigues comprando")
                    else:
                        print("sales de la tienda")
                        break
    elif accion==8:
        print("Decides no hacer nada y te vas a descansar")
        vida = 100
        estatus[2] ="relajada"
        dias+=1
    elif accion == 9:
        print("Revisas tus pertenencias")
        for cosa in inventario:
            print("Cosa")
        print("Miras la foto de tu familia... Hay cosas que no puedes cambiar, pero siempre la luz se antepone  a la oscuridad, esto es solo el inicio, no me voy a dar por vencida")
    else:
        print("NO PUEDES HACER ESO")

print("Ya ha llegado el dia, por fin te juntaras con el demonio mago ")
print("Antes de nada Cralvohz, te detiene para ver si vas presentable ante el mago")
if estatus[1] == "presentable":
    print("Cralvohz: Se ve bastante bien señorita, el mago la esta esperando")
elif estatus[1] =="bonita":
    print("Cralvohz: Dioses, señorita dejeme decirle que tiene usted un muy buen ojo para los atuendos, el mago la espera")
elif estatus[1] == "casi presentable":
    print("Cralvohz: Bueno se ve algo bien, no es lo mejor, pero seguro que el mago no lo nota")
elif estatus[1] == "casi decente":
    print("Cralvohz: Bueno se ve algo bien, no es lo mejor, pero seguro que el mago no lo nota")
elif estatus[1] == "decente":
    print("Cralvohz: Se ve bastante bien señorita, el mago la esta esperando")
else:
    print("Cralvohz: Si va con esos trapos mejor le doy prestada algo de ropa de mi hermana")
    print("Te pones la ropa que te presto el general demonio y partes a ver al mago")
print("Te sientes algo nerviosa por tener que conocer a alguien como tu, un mago, pero estas decidida a entender por que ese dragon ataco tu pueblo")
print("JUEGO TERMINADO NOS VEMOS EN EL ACTO III")
