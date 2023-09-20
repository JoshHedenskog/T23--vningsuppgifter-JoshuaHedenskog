x = 0
y = int(input("Hur många fåglar finns det?"))
z = y / 2 
å = str(input("Vad är förändringsfaktorn per år? mellan 0 och 1: "))
while (y > z):
    x = x + 1
    y = y * å
print ("Efter" , x , "år kommer andtalet fåglar ha halverats")