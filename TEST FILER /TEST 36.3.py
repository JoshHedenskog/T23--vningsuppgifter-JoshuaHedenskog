project_gran = 143
project_lotus = 232
operation_dove = 653
other = 404
password = int(input("Password:"))
if password == 18438:
    print ("Access Granted")
    print ("-")
    print ("Directories:")
    print ("143: Projekt Eula")
    print ("232: Project Lotus")
    print ("653: Operation Dove")
    print ("404: other;")
    print ("-")
    print ("-")
    print ("-")
    print ("-")
    print ("-")
    accesscode = int(input("Directory Code:"))
    if accesscode == 143:
        print ("/143")
        print ("(Project Eula)")
    if accesscode == 232:
        print ("/232")
        print ("(Project Lotus)")
    if accesscode == 653:
        print ("/653")
        print ("(Operation Dove)")
    if accesscode == 404:
        print ("/404")
        print ("(other)")
else:
    answer = int(input(">>incorrect password<<"))
    if answer == 18438:
        password = 18438

    
    
    
    





