år = int(input("Hej!, Ange ett år som du tror är ett skott år. Jag kommer då säga om det är det eller inte."))
år1 = år%4
år2 = år%100

if år1 == 0 and år2 != 0:
    print (år , "är ett skottår")
else:
    print (år , "är INTE ett skottår")

if år2 == 0:
    if (år%400) == 0:
        print (år , "är ett skottår")
    else:
        print (år , "är INTE ett skottår")

