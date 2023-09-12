namn = input("Hej, vad heter du?") 
print ("Hej" , namn , "! Detta program handlar om Boeing 787.")
print ("Här kommer 3 frågor om flyget:")
print ("-")
print ("När kom 787 ut?")
print ("-")
print ("val:")
print ("1: 2006")
print ("2: 2007")
print ("3: 2008")
print ("-")
svar1 = int(input("Svar:"))
print ("-")
if svar1 == 2:
    print ("rätt")
else:
    print ("fel, den kom ut 2007.")

print ("-")
print ("Hur många 787 varianter finns det?")
print ("-")
print ("val:")
print ("1: 2")
print ("2: 4")
print ("3: 3")
print ("-")
svar2 = int(input("Svar:"))
print ("-")
if svar2 == 3:
    print ("rätt")
else:
    print ("fel, det finns 3 varianter.")

print ("-")
print ("Vad är 787s smeknamn?")
print ("-")
print ("val:")
print ("1: Cloud")
print ("2: Dreamliner")
print ("3: Dreamlifter")
print ("-")
svar3 = int(input("Vad är 787 smeknamn?"))
if svar3 == 2:
    print ("rätt")
else:
    print ("fel, dens smaknamn är: Dreamliner")
print ("-")
if svar1 == 2:
    poäng1 = 1
else:
    poäng1 = 0

if svar2 == 3:
    poäng2 = 1
else:
    poäng2 = 0

if svar3 == 2:
    poäng3 = 1
else:
    poäng3 = 0
totalpoäng = poäng1 + poäng2 + poäng3 
if totalpoäng == 3:
    print ("Super! Du fick" , totalpoäng , "/ 3")
if totalpoäng == 2:
    print ("Bra jobbat! Du fick" , totalpoäng , "/ 3") 
if totalpoäng == 1:
    print ("Bra försök. Du fick" , totalpoäng , "/ 3")
if totalpoäng == 0:
    print ("Du fick" , totalpoäng , "/ 3. Du har i alla fall lärt dig något.")
print ("-")
print ("Tack så mycket för att du deltog i detta program")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")