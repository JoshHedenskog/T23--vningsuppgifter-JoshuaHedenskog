print ("Hej, välkommen till TLs biljett automat!\n-\nHur många ska köpa biljett? OBS: Max 4 i taget")
while True:
    customers = int(input("Svar: ")) 
    if customers >= 0:
        print ("Antalet måste vara högre än 0,försök igen")
    elif customers <= 4:
        print ("'Antalet måste vara lägre än 5, försök igen.")
    else:
        age = int(input("Hur gammal är du?"))
        if age <= 18:
            discount = 0.75 
        else:
            discount = 1
            print ("-\nBiljetter_\n-")               
            print ("1: 75 minuter -" , 50 * discount , "kr")
            print ("2: 24h -" , 120 * discount , "kr\n-")
            print ("3: 72h -" , 240 * discount , "kr\n-")
            val = int(input("Vilken biljett skulle du vilja ha?\nSvar: "))
            if val == 1:
                Person1 = 50 * discount
            if val == 2:
                Person1 = 120 * discount
            if val == 3:
                Person1 = 240 * discount
            if customers != (2 or 3 or 4):
                break