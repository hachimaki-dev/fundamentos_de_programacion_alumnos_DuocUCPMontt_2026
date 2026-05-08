
giga = 1
cobro_extra = 1000
giga_maxima = 15

while True: 
    print("1. Postpago")
    print("2. Prepago")

    plan = int(input("Que plan tiene?: "))
    GB = int(input("cuantas gigas utilizó?"))


    if plan == 2:
        print("Sin saldo")  
        break

    elif plan == 1: 

        if GB > giga_maxima:
            sobro = GB - giga_maxima
            total_a_pagar = sobro * cobro_extra
            print(total_a_pagar)
            


        


    