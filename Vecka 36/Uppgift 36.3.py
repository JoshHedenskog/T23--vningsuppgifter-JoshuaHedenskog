print ("Hej, välkommen till TLs biljett automat!\n-\nHur många ska köpa biljett? OBS: Max 4 i taget")
while True:
    customers = int(input("Svar: ")) 
    if customers <= 0:
        print ("Antalet måste vara högre än 0,försök igen")
    elif customers >= 5:
        print ("'Antalet måste vara lägre än 5, försök igen.")
    else:
        print ("Person 1:\n-")
        age = int(input("Hur gammal är du?"))
        if age <= 17:
            discount = 0.75 
        else:
            discount = 1
        print ("-\nBiljetter\n-")               
        print ("1: 75 minuter -" , 50 * discount , "kr\n-")
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
        else:
            print("Person 2:\n-")
            age2 = int(input("Hur gammal är du?"))
            if age2 <= 17:
                discount1 = 0.75 
            else:
                discount1 = 1
            print ("-\nBiljetter\n-")               
            print ("1: 75 minuter -" , 50 * discount1 , "kr\n-")
            print ("2: 24h -" , 120 * discount1 , "kr\n-")
            print ("3: 72h -" , 240 * discount1 , "kr\n-")
            val2 = int(input("Vilken biljett skulle du vilja ha?\nSvar: "))
            if val2 == 1:
                Person2 = 50 * discount1
            if val2 == 2:
                Person2 = 120 * discount1
            if val2 == 3:
                Person2 = 240 * discount1
            if customers != (3 or 4):
                break
            else:
                print("Person 2:\n-")
                age3 = int(input("Hur gammal är du?"))
                if age3 <= 17:
                    discount2 = 0.75 
                else:
                    discount2 = 1
                print ("-\nBiljetter\n-")               
                print ("1: 75 minuter -" , 50 * discount2 , "kr\n-")
                print ("2: 24h -" , 120 * discount2 , "kr\n-")
                print ("3: 72h -" , 240 * discount2 , "kr\n-")
                val3 = int(input("Vilken biljett skulle du vilja ha?\nSvar: "))
                if val3 == 1:
                    Person3 = 50 * discount2
                if val3 == 2:
                    Person3 = 120 * discount2
                if val3 == 3:
                    Person3 = 240 * discount2
                if customers != (4):
                    break
                else:
                    print("Person 2:\n-")
                    age4 = int(input("Hur gammal är du?"))
                    if age4 <= 17:
                        discount3 = 0.75 
                    else:
                        discount3 = 1
                    print ("-\nBiljetter\n-")               
                    print ("1: 75 minuter -" , 50 * discount3 , "kr\n-")
                    print ("2: 24h -" , 120 * discount3 , "kr\n-")
                    print ("3: 72h -" , 240 * discount3 , "kr\n-")
                    val4 = int(input("Vilken biljett skulle du vilja ha?\nSvar: "))
                    if val4 == 1:
                        Person4 = 50 * discount3
                    if val4 == 2:
                        Person4 = 120 * discount3
                    if val4 == 3:
                        Person4 = 240 * discount3
                    break
print ("Dina Biljetter: ")
print ("Person 1:" , Person1)
if customers >= 2:
    print ("Person 2:" , Person2)
if customers >= 3:
    print ("Person 3:" , Person3)
if customers >= 4:
    print ("Person 4:" , Person4)
#total = Person1 + Person1 + Person3 + Person4
#print ("\n-\n-\n-\nTotal:" , total , "kr\n-\n-\n-\n-")